# Synapsis People Counting System

Sistem ini mendeteksi, melacak, dan menghitung jumlah orang yang **masuk dan keluar** dari sebuah area tertentu dalam video menggunakan deteksi objek dan pelacakan centroid. Setiap aktivitas disimpan ke dalam database SQLite untuk keperluan analisis dan pencatatan (logging).

---
## 🗃️ Struktur Tabel Database

<img width="506" height="435" alt="image" src="https://github.com/user-attachments/assets/6323adff-59d6-4f0a-8eec-061315bd0859" />

<br>
<img width="501" height="359" alt="image" src="https://github.com/user-attachments/assets/3b8ef7a3-4528-447f-bdc9-c300a0b34a91" />

---

## 🧠 Fitur Utama

- Deteksi objek (fokus pada label `person`)
- Pelacakan menggunakan centroid tracker
- Polygonal ROI (Region of Interest) sebagai area hitung
- Hitung jumlah orang masuk & keluar dari area
- Simpan hasil ke database SQLite
- Logging ke file dan visualisasi real-time menggunakan OpenCV

---

## ⚙️ Instalasi

1. **Clone repo:**

```bash
git clone https://github.com/namamu/synapsis-people-counter.git
cd synapsis-people-counter
```

2. **Buat dan aktifkan virtual environment:**

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

3. **Install dependensi:**
```bash
pip install -r requirements.txt
```

🏃 **Menjalankan Sistem**

```bash
python scripts/run_pipeline.py
```

**Melihat hasil database:**
```bash
python scripts/view_db.py
```

## 📦 Dependensi Utama
* OpenCV
* NumPy
* SQLAlchemy
* Shapely
* tqdm (opsional)
* [YOLO model atau custom model] (melalui detection/detector.py)


## 📝 **Catatan**
Area dihitung menggunakan sebuah polygon kotak yang bisa disesuaikan.

ID objek tetap konsisten berkat CentroidTracker, memungkinkan pelacakan pergerakan masuk dan keluar secara akurat.

Database menggunakan SQLite untuk kemudahan setup dan pengujian lokal.



## ✅ Checklist Fitur dan Kendala

* Desain Database ✅ (Done)
 
  → Menggunakan SQLite dengan dua tabel: detections dan count_logs.
Tidak ada kendala berarti, namun int64 harus dikonversi sebelum disimpan ke JSON.

* Pengumpulan Dataset ✅ (Done)
  
  → Menggunakan video statis CCTV-JOGJA13s.mp4.
Tidak menggunakan live stream karena keterbatasan akses video real-time.

* Object Detection & Tracking ✅ (Done)
  
  → Menggunakan YOLO untuk deteksi objek (khusus label person) dan CentroidTracker untuk pelacakan.
Kendala: model deteksi tidak menangkap semua objek karena kualitas video.

* Counting & Polygon Area ✅ (Done)

  → Menggunakan polygon berbentuk kotak di posisi tengah layar, bisa digeser.
Menghitung masuk/keluar dengan logika pergerakan relatif terhadap area polygon.

* Prediksi (Forecasting) ❌ (X)

  → Belum diimplementasikan karena tidak termasuk prioritas utama.

* Integrasi API (API/Front End) ❌ (X)

  → Belum diimplementasikan. Fokus utama ada pada deteksi, tracking, counting, dan database.

* Deployment ❌ (X)

  → Belum menggunakan Docker. Proyek dijalankan secara lokal melalui virtual environment.
