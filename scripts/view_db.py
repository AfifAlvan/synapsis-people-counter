import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db import SessionLocal
from app.models import Detection, CountLog

db = SessionLocal()

print("=== Detections ===")
for det in db.query(Detection).all():
    print(f"{det.id}: {det.timestamp} | ID: {det.object_id} | Pos: {det.bbox} | In Area: {det.in_area}")

print("\n=== Count Logs ===")
for log in db.query(CountLog).all():
    print(f"{log.id}: {log.timestamp} | Area: {log.area_name} | {log.direction.upper()} | Count: {log.count}")
