import cv2
import os
import tkinter as tk
from tkinter import ttk, messagebox
from database.db import cek_users


class CaptureWajah(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Capture Wajah Mahasiswa")
        self.geometry("400x250")
        self.resizable(False, False)

        ttk.Label(self, text="Masukkan NIM:", font=("Arial", 12)).pack(pady=10)
        self.entry_nim = ttk.Entry(self, width=30)
        self.entry_nim.pack()

        ttk.Button(
            self, text="Mulai Capture", width=25, command=self.mulai_capture
        ).pack(pady=20)

    def mulai_capture(self):
        nim = self.entry_nim.get().strip()

        if nim == "":
            messagebox.showerror("Error", "NIM tidak boleh kosong!")
            return

        # Cek apakah NIM terdaftar
        data = cek_users(nim)
        if not data:
            messagebox.showerror("Error", "NIM tidak ditemukan di database!")
            return

        nama = data[0]

        # Siapkan folder dataset
        folder_path = f"dataset/{nim}"
        os.makedirs(folder_path, exist_ok=True)

        # Kamera
        cam = cv2.VideoCapture(0)
        detector = cv2.CascadeClassifier(
            "haarcascade/haarcascade_frontalface_default.xml"
        )

        count = 0

        messagebox.showinfo("Info", f"Mulai capture wajah untuk {nama} ({nim})")

        while True:
            ret, img = cam.read()
            if not ret:
                break

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)

            for x, y, w, h in faces:
                count += 1

                # Simpan wajah
                cv2.imwrite(
                    f"{folder_path}/{nama}.{nim}.{count}.jpg",
                    gray[y : y + h, x : x + w],
                )

                # Kotak wajah
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

                cv2.putText(
                    img,
                    f"Foto: {count}/50",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2,
                )

                cv2.imshow("Capture Wajah", img)

            if cv2.waitKey(1) == 27:  # ESC untuk stop manual
                break

            if count >= 50:  # jumlah foto
                break

        cam.release()
        cv2.destroyAllWindows()

        messagebox.showinfo("Selesai", f"Capture selesai! Total foto: {count}")
        self.destroy()
