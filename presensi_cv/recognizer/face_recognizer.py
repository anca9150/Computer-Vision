import cv2
import os
import numpy as np
from database.db import simpan_absensi, cek_users

TRAIN_FILE = "trainer/trainer.yml"
LABEL_FILE = "trainer/label_to_nim.npy"
CASCADE_FILE = "haarcascade/haarcascade_frontalface_default.xml"
CONFIDENCE_THRESHOLD = 50  # ubah sesuai kebutuhan


def mulai_absen():
    if not os.path.exists(TRAIN_FILE) or not os.path.exists(LABEL_FILE):
        print("Model belum ada, lakukan training dulu!")
        return False

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(TRAIN_FILE)
    label_to_nim = np.load(LABEL_FILE, allow_pickle=True).item()

    detector = cv2.CascadeClassifier(CASCADE_FILE)
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX

    absensi_count = 0
    absensi_done = set()  # track NIM yang sudah absen

    print("Mulai absensi wajah... Tekan ESC untuk berhenti.")

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)

        for x, y, w, h in faces:
            label_pred, confidence = recognizer.predict(gray[y : y + h, x : x + w])
            nim_pred = label_to_nim[label_pred]

            if confidence > CONFIDENCE_THRESHOLD:
                nama = None
            else:
                nama = cek_users(nim_pred)

            if nama:
                nama = nama[0]
                if nim_pred not in absensi_done:
                    simpan_absensi(nim_pred, nama)
                    absensi_count += 1
                    absensi_done.add(nim_pred)
                label_text = f"{nama} ({nim_pred}) - {confidence:.2f}"
                color = (0, 255, 0)
            else:
                label_text = f"Unknown - {confidence:.2f}"
                color = (0, 0, 255)

            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label_text, (x, y - 10), font, 0.7, color, 2)

        cv2.imshow("Absensi Wajah - Tekan ESC untuk berhenti", frame)
        if cv2.waitKey(1) == 27:
            break

    cam.release()
    cv2.destroyAllWindows()
    print(f"Total absensi berhasil: {absensi_count}")
    return absensi_count


if __name__ == "__main__":
    mulai_absen()
