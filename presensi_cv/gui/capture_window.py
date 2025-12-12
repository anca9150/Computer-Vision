import tkinter as tk
from tkinter import ttk, messagebox
from capture.face_capture import capture_faces
from database.db import cek_users


class CaptureWindow(tk.Toplevel):
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

        data = cek_users(nim)
        if not data:
            messagebox.showerror("Error", "NIM belum terdaftar")
            return

        nama = data[0]
        messagebox.showinfo("Info", f"Mulai capture wajah untuk {nama} ({nim})")

        jumlah = capture_faces(nim, nama)
        messagebox.showinfo("Selesai", f"Capture selesai! Total foto: {jumlah}")
        self.destroy()
