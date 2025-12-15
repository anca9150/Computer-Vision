from openpyxl import Workbook
from database.db import get_absensi
from datetime import datetime
import os


def export_absensi_excel():
    data = get_absensi()

    if not data:
        return False

    wb = Workbook()
    ws = wb.active
    ws.title = "Presensi"

    # Header
    ws.append(["NIM", "Nama", "Waktu"])

    # Data
    for row in data:
        ws.append(row)

    os.makedirs("Exports", exist_ok=True)

    filename = f"exports/presensi_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    wb.save(filename)

    return filename
