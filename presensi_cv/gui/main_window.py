import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from gui.mahasiswa_form import FormMahasiswa
from gui.capture_window import CaptureWindow
from gui.trining_window import TrainingWindow
from gui.absensi_window import AbsensiWindow
from gui.rekap_window import RekapWindow


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Judul aplikasi
        self.title("Aplikasi Presensi Computer Vision")
        self.geometry("600x400")
        self.resizable(False, False)

        # Judul utama
        title_label = tk.Label(
            self, text="APLIKASI PRESENSI COMPUTER VISION", font=("Arial", 16, "bold")
        )
        title_label.pack(pady=20)

        # Frame menu
        frame = tk.Frame(self)
        frame.pack(pady=20)

        # Tombol
        btn_users = ttk.Button(
            frame, text="Input Data Mahasiswa", width=30, command=self.menu_mahasiswa
        )
        btn_users.grid(row=0, column=0, pady=5)

        btn_capture = ttk.Button(
            frame, text="Capture Wajah", width=30, command=self.menu_capture
        )
        btn_capture.grid(row=1, column=0, pady=5)

        btn_train = ttk.Button(
            frame, text="Training Wajah", width=30, command=self.menu_train
        )
        btn_train.grid(row=2, column=0, pady=5)

        btn_absen = ttk.Button(
            frame, text="Mulai Absensi", width=30, command=self.menu_absen
        )
        btn_absen.grid(row=3, column=0, pady=5)

        btn_rekap = ttk.Button(
            frame, text="Rekap Presensi", width=30, command=self.menu_rekap
        )
        btn_rekap.grid(row=4, column=0, pady=5)

    # Placeholder fungsi menu

    def menu_mahasiswa(self):
        FormMahasiswa(self)

    def menu_capture(self):
        CaptureWindow(self)

    def menu_train(self):
        TrainingWindow(self)

    def menu_absen(self):
        AbsensiWindow(self)

    def menu_rekap(self):
        RekapWindow(self)
