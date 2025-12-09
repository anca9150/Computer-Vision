import cv2
import os
import numpy as np
import json
from pathlib import Path

DATASET_DIR = Path("dataset")
MODEL_FILE = Path("face_model.xml")
LABELS_FILE = Path("labels.json")

if not DATASET_DIR.exists():
    print("Folder dataset/ tidak ditemukan")
    exit()

faces = []
labels = []
label_to_name = {}
current_label = 0

for person_folder in DATASET_DIR.iterdir():
    if person_folder.is_dir():
        name = person_folder.name
        label_to_name[current_label] = name

        for img_file in person_folder.glob("*.jpg"):
            img = cv2.imread(str(img_file), cv2.IMREAD_GRAYSCALE)
            if img is None:
                continue
            faces.append(img)
            labels.append(current_label)

        current_label += 1

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(labels))
recognizer.save(str(MODEL_FILE))

with open(LABELS_FILE, "w") as f:
    json.dump(label_to_name, f, indent=4)

print("Training selesai!")
print(f"Model tersimpan di: {MODEL_FILE}")
print(f"MApping label tersimpan di: {LABELS_FILE}")
print(f"Total mahasiswa: {len(label_to_name)}")
