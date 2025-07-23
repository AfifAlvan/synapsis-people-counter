import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db import Base, engine
from app import models

# Membuat semua tabel berdasarkan deklarasi model
Base.metadata.create_all(bind=engine)
print("✅ Semua tabel berhasil dibuat di database.db")
