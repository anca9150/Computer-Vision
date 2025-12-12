import tkinter as tk
from tkinter import ttk, messagebox
from database.db import tambah_mahasiswa


class FormMahasiswa(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Input Data Mahasiswa")
        self.geometry("400x250")
        self.resizable(False, False)

        # Label dan input
        ttk.Label(self, text="NIM: ", font=("Arial", 12)).pack(pady=10)
        self.entry_nim = ttk.Entry(self, width=30)
        self.entry_nim.pack()

        ttk.Label(self, text="Nama: ", font=("Arial", 12)).pack(pady=10)
        self.entry_nama = ttk.Entry(self, width=30)
        self.entry_nama.pack()

        # Tombol simpan
        ttk.Button(self, text="Simpan", width=20, command=self.simpan_data).pack(
            pady=20
        )

    def simpan_data(self):
        nim = self.entry_nim.get().strip()
        nama = self.entry_nama.get().strip()

        if nim == "" or nama == "":
            messagebox.showerror("Error", "NIM dan Nama tidak boleh kosong!")
            return

        # Simpan ke database
        hasil = tambah_mahasiswa(nim, nama)

        if hasil:
            messagebox.showinfo("Berhasil", "Data mahasiswa berhasil disimpan!")
            self.destroy()
        else:
            messagebox.showerror("Gagal", "NIM sudah terdaftar atau terjadi error.")
