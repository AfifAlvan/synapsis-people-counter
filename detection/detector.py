# from ultralytics import YOLO
# import cv2

# model = YOLO('yolov8n.pt')  # or yolov5s.pt

# def detect_people(frame):
#     results = model(frame)
#     boxes = []
#     for r in results:
#         for box in r.boxes:
#             if int(box.cls[0]) == 0:  # class 0 = person
#                 x1, y1, x2, y2 = map(int, box.xyxy[0])
#                 boxes.append((x1, y1, x2, y2))
#     return boxes
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # pastikan sudah install dan model tersedia
TARGET_CLASSES = {"person", "car", "motorbike", "bus"}

def detect_people(frame):
    results = model(frame)[0]
    boxes = []
    classes = []
    for box in results.boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        if label in TARGET_CLASSES:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            boxes.append([x1, y1, x2, y2])
            classes.append(label)
    return boxes, classes
