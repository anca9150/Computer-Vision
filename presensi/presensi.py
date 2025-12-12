import cv2
import mysql.connector
import datetime

# Load LBPH model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/trainer.yml")

# Load Haarcascade
face_cascade = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")

# Koneksi ke MySQL
db = mysql.connector.connect(
    host="localhost", user="root", password="", database="da_presensi"
)

cursor = db.cursor()

# Ambil data mahasiswa dari DB
cursor.execute("SELECT nim, nama FROM users")
data_usr = cursor.fetchall()

# Buat dictionary {nim: nama}
usr_dict = {int(nim): nama for nim, nama in data_usr}

# Start webcam
cam = cv2.VideoCapture(0)

print("Sistem Presensi Siap. Tekan Q untuk keluar.")

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for x, y, w, h in faces:
        id_predicted, confidence = recognizer.predict(gray[y : y + h, x : x + w])

        # Tampilkan kotak wajah
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if confidence < 60:  # semakin kecil semakin kurat
            nama = usr_dict.get(id_predicted, "Tidak dikenal")

            # Tampilkan nama di frame
            cv2.putText(
                frame,
                nama,
                (x + 5, y - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2,
            )

            # Simpan presensi ke DB
            cursor.execute("INSERT INTO presensi (nim) VALUES ($s)", (id_predicted,))
            db.commit()

            print("✔ Presensi berhasil untuk: ", nama)

        else:
            cv2.putText(
                frame,
                "Tidak dikenal",
                (x + 5, y - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2,
            )

    cv2.imshow("Presensi Wajah", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
