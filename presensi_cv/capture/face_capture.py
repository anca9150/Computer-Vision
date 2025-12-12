import cv2
import os


def capture_faces(nim, nama, jumlah=50):
    # Siapkan folder dataset
    folder_path = f"dataset/{nim}"
    os.makedirs(folder_path, exist_ok=True)

    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")

    count = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)

        for x, y, w, h in faces:
            count += 1
            # Simpan wajah
            cv2.imwrite(
                f"{folder_path}/{nama}.{nim}.{count}.jpg", gray[y : y + h, x : x + w]
            )
            # Kotak wajah
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(
                frame,
                f"Foto: {count}/{jumlah}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2,
            )

        cv2.imshow("Capture Wajah", frame)

        if cv2.waitKey(1) == 27 or count >= jumlah:  # ESC atau jumlah foto
            break

    cam.release()
    cv2.destroyAllWindows()
    return count
