import tkinter as tk
from tkinter import ttk, messagebox
from database.db import get_absensi_by_date
from datetime import date
from utils.export_excel import export_absensi_excel


class RekapWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Rekap Presensi")
        self.geometry("600x400")

        ttk.Label(self, text="Tanggal (YYYY-MM-DD):").pack(pady=5)
        self.entry_tanggal = ttk.Entry(self)
        self.entry_tanggal.pack()
        self.entry_tanggal.insert(0, str(date.today()))

        ttk.Button(self, text="Tampilkan", width=20, command=self.load_data).pack(
            pady=10
        )

        ttk.Button(
            self, text="Export ke Excel", width=20, command=self.export_excel
        ).pack(pady=10)

        self.tree = ttk.Treeview(
            self, columns=("nim", "nama", "waktu"), show="headings"
        )
        self.tree.heading("nim", text="NIM")
        self.tree.heading("nama", text="Nama")
        self.tree.heading("waktu", text="Waktu Absen")
        self.tree.pack(fill=tk.BOTH, expand=True)

    def load_data(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        tanggal = self.entry_tanggal.get()
        data = get_absensi_by_date(tanggal)

        for row in data:
            self.tree.insert("", tk.END, values=row)

    def export_excel(self):
        hasil = export_absensi_excel()
        if hasil:
            messagebox.showinfo("Berhasil", f"Data berhasil diexport:\n{hasil}")
        else:
            messagebox.showwarning("Kosong", "Data presensi masih kosong.")
