import cv2
import os
from pathlib import Path


# Folder dataset
DATASET_DIR = Path("dataset")
DATASET_DIR.mkdir(exist_ok=True)

# Input NIM dan Nama
nim = input("Masukkan NIM: ")
nama = input("Masukkan Nama: ")

folder = DATASET_DIR / f"{nim}_{nama.replace(' ', '_')}"
folder.mkdir(exist_ok=True)

# Load Haar Cascade
cascade_path = "haarcascade/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)
if face_cascade.empty():
    print("Error: Haarcascade tidak ditemukan di folder haarcascade/")
    exit()

# Nyalakan kamera
cam = cv2.VideoCapture(0)

count = 0
MAX_IMAGES = 20  # jumlah foto per mahasiswa

print("Tekan 'q' untuk keluar lebih cepat.")

while count < MAX_IMAGES:
    ret, frame = cam.read()
    if not ret:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for x, y, w, h in faces:
        face_img = frame[y : y + h, x : x + w]
        # simpan foto
        cv2.imwrite(str(folder / f"{count+1}.jpg"), face_img)
        count += 1
        # tampilkan kotak di wajah
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Capture Dataset", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    if count >= MAX_IMAGES:
        break

cam.release()
cv2.destroyAllWindows()
print(f"Dataset selesai untuk {nama}. Total foto: {count}")
