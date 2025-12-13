import tkinter as tk
from tkinter import ttk, messagebox
from recognizer.face_recognizer import mulai_absen


class AbsensiWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Mode Absensi Wajah")
        self.geometry("400x200")
        self.resizable(False, False)

        ttk.Label(
            self, text="Mulai absensi dengan pengenalan wajah", font=("Arial", 12)
        ).pack(pady=20)
        ttk.Button(self, text="Mulai Absensi", width=25, command=self.mulai).pack(
            pady=10
        )

    def mulai(self):
        jumlah = mulai_absen()
        messagebox.showinfo(
            "Selesai", f"Absensi selesai! Total mahasiswa terdeteksi: {jumlah}"
        )
        self.destroy()
