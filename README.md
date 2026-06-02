# 🎓 AI Proctor System

An AI-powered online exam proctoring system built using OpenCV and MediaPipe. The system monitors candidates in real time through a webcam, detects suspicious activities, logs incidents, captures evidence, and maintains an integrity score to support secure online examinations.

---

## 🚀 Features

### 👤 Face Detection

* Detects the candidate's face in real time.
* Tracks facial landmarks using MediaPipe Face Landmarker.

### 👀 Head Movement Monitoring

* Detects:

  * Looking Left
  * Looking Right
  * Looking Up
  * Looking Down
  * Looking Center

### 🚫 Multiple Face Detection

* Instantly terminates the session if more than one face is detected.

### ❌ No Face Detection

* Records violations when the candidate leaves the camera view.

### 📸 Evidence Collection

* Automatically captures screenshots of suspicious activities.
* Stores evidence images in the `evidence/` directory.

### 📝 Event Logging

* Records all violations in a CSV log file.
* Includes:

  * Timestamp
  * Event Type
  * Current Score

### 📊 Integrity Score System

* Starts with a score of 100.
* Deducts points for suspicious behavior.
* Terminates the session after repeated violations.

---

## 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe Face Landmarker
* CSV Logging
* Computer Vision

---

## 📂 Project Structure

```text
AI-Proctor-System/
│
├── face_landmarker.task
├── main.py
├── log.csv
├── evidence/
│   ├── 1712345678.jpg
│   ├── 1712345689.jpg
│   └── ...
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Proctor-System.git
cd AI-Proctor-System
```

### 2. Install Dependencies

```bash
pip install opencv-python mediapipe
```

### 3. Download Face Landmarker Model

Download the MediaPipe Face Landmarker model and place it in the project root directory:

```text
face_landmarker.task
```

---

## ▶️ Running the Project

```bash
python main.py
```

Press:

```text
Q
```

to quit the application.

---

## 📋 Violation Rules

| Event               | Penalty               |
| ------------------- | --------------------- |
| Looking Away        | -2 Points             |
| No Face Detected    | -5 Points             |
| Multiple Faces      | Immediate Termination |
| Repeated Violations | Exam Termination      |

---

## 📈 Output

### Live Monitoring Window

Displays:

* Face Tracking
* Current Status
* Integrity Score

### Log File

Example:

```csv
Time,Event,Score
10:21:15,Looking Left,98
10:21:20,No Face,93
10:21:25,Looking Right,91
```

### Evidence Folder

Automatically stores screenshots of suspicious events:

```text
evidence/
├── 1712345678.jpg
├── 1712345689.jpg
└── ...
```

---

## 🔒 Use Cases

* Online Examinations
* Remote Assessments
* Certification Tests
* E-Learning Platforms
* Academic Integrity Monitoring

---

## 🔮 Future Improvements

* Eye Gaze Tracking
* Mobile Phone Detection
* Person Identification
* Audio Monitoring
* Browser Activity Monitoring
* Cloud-Based Reporting Dashboard
* Machine Learning-Based Behavior Analysis

---

## 🤝 Contributing

Contributions, feature requests, and improvements are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Aryan Kadbe

Computer Science & Cybersecurity Student

Building AI and cybersecurity projects focused on automation, computer vision, and digital security.

