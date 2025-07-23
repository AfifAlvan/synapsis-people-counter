# Synapsis People Counting System

Sistem ini mendeteksi, melacak, dan menghitung jumlah orang yang **masuk dan keluar** dari sebuah area tertentu dalam video menggunakan deteksi objek dan pelacakan centroid. Setiap aktivitas disimpan ke dalam database SQLite untuk keperluan analisis dan pencatatan (logging).

---

## 📁 Struktur Proyek

Synapsis/
├── app/
│ ├── db.py # Konfigurasi database
│ ├── models.py # Definisi tabel Detection & CountLog
├── data/
│ ├── videos/ # Folder video input (contoh: CCTV-JOGJA13s.mp4)
│ └── outputs/ # Folder output (log.txt, dll.)
├── detection/
│ ├── detector.py # Fungsi deteksi orang
│ └── tracker.py # Pelacak objek (CentroidTracker)
├── scripts/
│ ├── run_pipeline.py # Main script untuk menjalankan deteksi + counting
│ └── view_db.py # Menampilkan isi database (Detection dan CountLog)
├── README.md # Dokumentasi ini
└── requirements.txt # Daftar library yang dibutuhkan



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

2. **Buat dan aktifkan virtual environment:**

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows

```bash
2. **Install dependensi:**
pip install -r requirements.txt

🏃 **Menjalankan Sistem**

```bash
python scripts/run_pipeline.py

**Melihat hasil database:**
```bash
python scripts/view_db.py


📦 Dependensi Utama
* OpenCV
* NumPy
* SQLAlchemy
* Shapely
* tqdm (opsional)
* [YOLO model atau custom model] (melalui detection/detector.py)


📝 **Catatan**
Area dihitung menggunakan sebuah polygon kotak yang bisa disesuaikan.

ID objek tetap konsisten berkat CentroidTracker, memungkinkan pelacakan pergerakan masuk dan keluar secara akurat.

Database menggunakan SQLite untuk kemudahan setup dan pengujian lokal.