import tkinter as tk
from tkinter import ttk, messagebox
from trainer.face_training import train_faces


class TrainingWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Training Wajah")
        self.geometry("400x200")
        self.resizable(False, False)

        ttk.Label(self, text="Training model LBPH wajah", font=("Arial", 12)).pack(
            pady=20
        )
        ttk.Button(
            self, text="Mulai Training", width=25, command=self.mulai_training
        ).pack(pady=10)

    def mulai_training(self):
        hasil = train_faces()
        if hasil:
            messagebox.showinfo("Selesai", "Training model selesai!")
        else:
            messagebox.showerror("Gagal", "Training gagal. Dataset kosong atau error.")
