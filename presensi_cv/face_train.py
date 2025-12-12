import cv2
import numpy as np
from PIL import Image
import os

# Path dataset
dataset_path = "dataset"

# LBPH face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Detector wajah
detector = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")


def get_images_and_labels(path):
    face_samples = []
    ids = []

    # Loop tiap folder (nama.nim)
    for folder_name in os.listdir(path):
        folder_path = os.path.join(path, folder_name)

        if not os.path.isdir(folder_path):
            continue  # skip jika bukan folder

        # Loop setiap file dalam folder
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            # Pastikan file adalah gambar
            if not file_name.lower().endswith((".jpg", ".png", ".jpeg")):
                continue

            # Convert gambar ke grayscale
            img = Image.open(file_path).convert("L")
            img_np = np.array(img, "uint8")

            # Extract NIM
            try:
                nim = int(file_name.split(".")[1])
            except:
                print("Format nama file salah:", file_name)
                continue

            # Deteksi wajah
            faces = detector.detectMultiScale(img_np)

            for x, y, w, h in faces:
                face_samples.append(img_np[y : y + h, x : x + w])
                ids.append(nim)

    return face_samples, ids


print("Sedang melakukan training wajah...")

faces, ids = get_images_and_labels(dataset_path)

print("Jumlah wajah terbaca:", len(faces))
print("Jumlah ID terbaca:", len(ids))

# Minimal 1 wajah untuk training
if len(faces) == 0:
    raise Exception(
        "Tidak ditemukan data wajah. Pastikan dataset berisi gambar dan wajah terdeteksi."
    )

# Training
recognizer.train(faces, np.array(ids))

# Simpan hasil
os.makedirs("trainer", exist_ok=True)
recognizer.write("trainer/trainer.yml")

print("Training selesai! File model tersimpan di trainer/trainer.yml")
