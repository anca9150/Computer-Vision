import cv2
import os

# Load detector wajah
face_detector = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")

# Input data mahasiswa
nim = input("Masukkan NIM: ")
nama = input("Masukkan Nama: ")

# Buat folder berdasarkan NIM
folder_path = f"dataset/{nim}"
os.makedirs(folder_path, exist_ok=True)

cam = cv2.VideoCapture(0)

print("Mengambil gambar. Tekan esc untuk berhenti.")

count = 0

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for x, y, w, h in faces:
        count += 1
        #   Simpan gambar wajah ke folder NIM
        file_name = f"{folder_path}/{nama}.{nim}.{count}.jpg"
        cv2.imwrite(file_name, gray[y : y + h, x : x + w])

        #   Kotak wajah
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Pengambilan Dataset", frame)

    key = cv2.waitKey(1)
    if key == 27:  # Esc
        break
    elif count >= 50:
        break

cam.release()
cv2.destroyAllWindows()

print(f"Dataset wajah tersimpan untuk NIM {nim}. Total gambar: {count}")
