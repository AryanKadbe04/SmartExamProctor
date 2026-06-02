import cv2
import mediapipe as mp
import time
import csv
import os

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# -------- LOAD MODEL --------

base_options = python.BaseOptions(model_asset_path="face_landmarker.task")

options = vision.FaceLandmarkerOptions(
    base_options=base_options,
    output_face_blendshapes=True,
    num_faces=2
)

detector = vision.FaceLandmarker.create_from_options(options)

# -------- CAMERA --------
cap = cv2.VideoCapture(0)

score = 100
last_penalty = 0

# -------- CHEATING CONTROL --------
cheat_count = 0
CHEAT_LIMIT = 5

# -------- FILE SETUP --------
if not os.path.exists("evidence"):
    os.makedirs("evidence")

file = open("log.csv", "w", newline="", buffering=1)
writer = csv.writer(file)
writer.writerow(["Time", "Event", "Score"])

def log(event):
    global score
    t = time.strftime("%H:%M:%S")
    print(t, event, score)
    writer.writerow([t, event, score])

def save_img(frame):
    cv2.imwrite(f"evidence/{int(time.time())}.jpg", frame)

# -------- LOOP --------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    result = detector.detect(mp_image)

    warning = ""
    now = time.time()

    if result.face_landmarks:

        # MULTIPLE FACE → TERMINATE
        if len(result.face_landmarks) > 1:
            log("Multiple Faces - TERMINATED")
            save_img(frame)

            cv2.putText(frame, "CHEATING DETECTED!", (50,200),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
            cv2.imshow(" AI PROCTOR", frame)
            cv2.waitKey(3000)
            break

        for face_landmarks in result.face_landmarks:

            # Nose landmark
            nose = face_landmarks[1]

            x = int(nose.x * w)
            y = int(nose.y * h)

            cv2.circle(frame, (x, y), 5, (0,255,0), -1)

        # -------- FULL DIRECTION DETECTION --------
        if nose.x < 0.4:
            warning = "Looking Left"
        elif nose.x > 0.6:
            warning = "Looking Right"
        elif nose.y > 0.65:
            warning = "Looking Down"
        elif nose.y < 0.35:
             warning = "Looking Up"
        else:
            warning = "Looking Center"

            #  CHEATING COUNT
            if warning != "Looking Center":
                if now - last_penalty > 2:
                    cheat_count += 1
                    score -= 2
                    log(warning)
                    save_img(frame)
                    last_penalty = now

            #  CHEATING LIMIT EXCEEDED
            if cheat_count >= CHEAT_LIMIT:
                log("Cheating Limit Exceeded - TERMINATED")
                save_img(frame)

                cv2.putText(frame, "EXAM TERMINATED!", (50,200),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
                cv2.imshow(" AI PROCTOR", frame)
                cv2.waitKey(3000)
                break

    else:
        warning = "No Face"
        if now - last_penalty > 2:
            cheat_count += 1
            score -= 5
            log(warning)
            save_img(frame)
            last_penalty = now

    # -------- DISPLAY --------
    if warning:
        cv2.putText(frame, warning, (50,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.putText(frame, f"Score: {score}", (50,100),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow(" AI PROCTOR SYSTEM", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -------- CLEANUP --------
cap.release()
file.close()
cv2.destroyAllWindows()