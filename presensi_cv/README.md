# 📸 Sistem Presensi Mahasiswa Berbasis Pengenalan Wajah (Computer Vision)

Aplikasi presensi mahasiswa berbasis **Computer Vision** menggunakan **Python, OpenCV (LBPH Face Recognition), Tkinter GUI, dan MySQL**.  
Sistem ini memungkinkan dosen melakukan presensi otomatis melalui kamera dengan hasil rekap yang dapat diekspor ke Excel.

---

## 🎯 Fitur Utama

- Registrasi & pengenalan wajah mahasiswa
- Presensi real-time menggunakan kamera
- Satu wajah hanya tercatat **1 kali presensi per hari**
- Rekap presensi harian
- Export presensi ke **Excel (.xlsx)**
- GUI desktop menggunakan **Tkinter**
- Database MySQL sebagai penyimpanan data

---

## 🧠 Teknologi yang Digunakan

- Python 3
- OpenCV (LBPH Face Recognizer)
- Tkinter
- MySQL
- OpenPyXL
- Haar Cascade Classifier

---

## 📂 Struktur Folder

presensi_cv/
│
├── app.py
├── dataset/ # Dataset wajah (di-ignore Git)
│ └── .gitkeep
│
├── trainer/ # Model hasil training (di-ignore Git)
│ └── .gitkeep
│
├── haarcascade/
│ └── haarcascade_frontalface_default.xml
│
├── gui/
│ ├── main_window.py
│ ├── absensi_window.py
│ └── rekap_window.py
│
├── recognizer/
│ └── face_recognizer.py
│
├── database/
│ └── db.py
│
├── utils/
│ └── export_excel.py
│
├── config/
│ └── db_config.py
│
├── .gitignore
└── README.md

**Catatan:**  
Folder `dataset/` dan `trainer/` tidak berisi data di repository karena:

- Menjaga privasi data wajah
- Ukuran file besar
- Model dapat dibuat ulang melalui proses training
