import cv2
import numpy as np
from detection.detector import detect_people
from detection.tracker import CentroidTracker
from shapely.geometry import Point, Polygon
from datetime import datetime
from app.db import SessionLocal
from app.models import Detection, CountLog
import os

# Setup DB
db = SessionLocal()

# Setup tracker
tracker = CentroidTracker(maxDisappeared=20)
prev_positions = {}

# Buka video
video_path = "data/videos/CCTV-JOGJA13s.mp4"
cap = cv2.VideoCapture(video_path)

# Buat folder output
os.makedirs("data/outputs", exist_ok=True)

# Counter total
total_in, total_out = 0, 0

# Ambil ukuran frame
ret, frame = cap.read()
if not ret:
    raise ValueError("Tidak bisa membaca frame pertama")
frame_height, frame_width = frame.shape[:2]
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# Polygon area (geser 40% ke kiri)
box_w, box_h = 200, 200
cx, cy = frame_width // 2, frame_height // 2
cx -= int(frame_width * 0.4)
polygon_coords = [
    (cx - box_w // 2, cy - box_h // 2),
    (cx + box_w // 2, cy - box_h // 2),
    (cx + box_w // 2, cy + box_h // 2),
    (cx - box_w // 2, cy + box_h // 2),
]
polygon = Polygon(polygon_coords)
polygon_name = "Area 1"

print(f"[DEBUG] Polygon Coords: {polygon_coords}")

# Fungsi menghitung masuk/keluar
def count_people(objects, polygon, prev_positions):
    masuk, keluar = 0, 0
    inside_ids = []

    for obj_id, (x, y) in objects.items():
        now = Point(x, y)
        inside_now = polygon.contains(now)

        if inside_now:
            inside_ids.append(obj_id)

        if obj_id in prev_positions:
            was_inside = prev_positions[obj_id]["inside"]
            if not was_inside and inside_now:
                masuk += 1
            elif was_inside and not inside_now:
                keluar += 1
        else:
            if inside_now:
                masuk += 1

        prev_positions[obj_id] = {"pos": (x, y), "inside": inside_now}

    return masuk, keluar, inside_ids

# Loop utama
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    timestamp = datetime.now()

    # Deteksi objek
    boxes, labels = detect_people(frame)
    person_boxes = [box for box, label in zip(boxes, labels) if label == 'person']

    # Tracking
    objects = tracker.update(person_boxes)

    # Hitung masuk / keluar
    c_in, c_out, inside_ids = count_people(objects, polygon, prev_positions)
    total_in += c_in
    total_out += c_out

    # Simpan log count jika ada perubahan
    if c_in > 0:
        db.add(CountLog(
            timestamp=timestamp,
            area_name=polygon_name,
            direction="in",
            count=c_in
        ))
    if c_out > 0:
        db.add(CountLog(
            timestamp=timestamp,
            area_name=polygon_name,
            direction="out",
            count=c_out
        ))

    # Simpan deteksi setiap objek
    for obj_id, (x, y) in objects.items():
        det = Detection(
            timestamp=timestamp,
            object_id=int(obj_id),
            bbox={"x": int(x), "y": int(y)},
            area_name=polygon_name,
            in_area=polygon.contains(Point(x, y))
        )
        db.add(det)

    db.commit()

    # Visualisasi
    for (x1, y1, x2, y2) in person_boxes:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    for obj_id, (x, y) in objects.items():
        inside = polygon.contains(Point(x, y))
        color = (0, 255, 0) if inside else (0, 0, 255)
        cv2.circle(frame, (x, y), 5, color, -1)
        cv2.putText(frame, f"ID {obj_id}", (x, y - 10), 0, 0.5, (255, 255, 0), 1)

    # Gambar polygon
    cv2.polylines(frame, [np.array(polygon_coords, np.int32)], True, (0, 0, 255), 2)
    cv2.putText(frame, f"Masuk: {total_in} | Keluar: {total_out}", (10, 30), 0, 1, (255, 255, 255), 2)

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Ringkasan
print("\n===== RINGKASAN DETEKSI =====")
print(f"Total orang masuk area: {total_in}")
print(f"Total orang keluar area: {total_out}")

# Cleanup
cap.release()
cv2.destroyAllWindows()
