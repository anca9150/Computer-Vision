from config.db_config import get_connection


# Fungsi tambah mahasiswa
def tambah_mahasiswa(nim, nama):
    db = get_connection()
    cursor = db.cursor()
    sql = "INSERT INTO users (nim, nama), VALUES (%s, %s)"
    try:
        cursor.execute(sql, (nim, nama))
        db.commit()
        return True
    except:
        return False
    finally:
        cursor.close()
        db.close()


# Fungsi ambil semua users
def get_all_users():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data


# Cek apakah user terdaftar
def cek_users(nim):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT nama FROM users WHERE nim=%s", (nim,))
    hasil = cursor.fetchone()
    cursor.close()
    db.close()
    return hasil


# Simpan absensi
def simpan_absensi(nim, nama):
    db = get_connection()
    cursor = db.cursor()
    sql = "INSERT INTO absensi (nim, nama) VALUES (%s, %s)"
    cursor.execute(sql, (nim, nama))
    db.commit()
    cursor.close()
    db.close()


# Ambil semua data absensi
def get_absensi():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM absensi ORDER BY waktu DESC")
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data
