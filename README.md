# 🖱️ Air Mouse – Gesture Controlled Virtual Mouse

Control your computer cursor using **hand gestures via webcam**.  
This project uses **computer vision + real-time hand tracking** to replace a physical mouse with intuitive finger movements.

---

## 🚀 Features

✅ Smooth cursor movement using index finger  
✅ Click & Drag via thumb–index pinch  
✅ Scroll control using index–middle pinch  
✅ Dynamic cursor smoothing for stability  
✅ Pause control using fist gesture ✊  
✅ Bounding box for precision tracking  
✅ Real-time FPS counter  
✅ Visual gesture state indicators  

---

## 🧠 How It Works

The system follows a real-time vision pipeline:

1. 📷 **Webcam Feed (OpenCV)** – Captures live video frames  
2. ✋ **Hand Tracking (MediaPipe)** – Detects 21 hand landmarks  
3. 🎯 **Landmark Processing** – Extracts finger coordinates  
4. 🖥️ **Coordinate Mapping** – Converts camera space → screen space  
5. 🌀 **Dynamic Smoothing** – Reduces jitter & noise  
6. 🖱️ **Mouse Control (PyAutoGUI)** – Sends OS cursor events  

---

## 🛠️ Tech Stack

- **Python**
- **OpenCV** – Video capture & frame processing
- **MediaPipe** – Hand landmark detection
- **PyAutoGUI** – System cursor control
- **NumPy** – Coordinate interpolation & math

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AirMouse.git
cd AirMouse
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

Press **Q** to exit.

---

## 🎮 Controls & Gestures

| Gesture | Action |
|---------|--------|
| ☝ Index Finger Move | Cursor Movement |
| 🤏 Thumb + Index Pinch | Click / Drag |
| 🤏 Index + Middle Pinch | Scroll |
| ✊ Fist Gesture | Pause Cursor |

---

## 🎯 Stability & UX Improvements

This project focuses heavily on **real-world usability**:

✔ Dynamic smoothing based on hand velocity  
✔ Dead-zone filtering to prevent jitter  
✔ Click debouncing to avoid false triggers  
✔ Movement bounding box for precision  
✔ Noise-resilient gesture detection  

---

## ⚡ Performance Considerations

- Optimized for real-time interaction
- Low-resolution frame processing for reduced CPU load
- Minimal latency cursor mapping
- FPS monitoring for performance visibility

---

## 💡 Best Usage Conditions

✅ Good lighting environment  
✅ Clear hand visibility  
✅ Hand inside bounding box  
✅ Avoid background clutter  

---

## 📸 Demo Preview (Recommended)

Add a demo GIF or video here for maximum impact:

```
/assets/demo.gif
```

Example:

![Demo](assets/demo.gif)

---

## 🧩 Possible Extensions

- Multi-hand support
- Gesture customization UI
- Air drawing / annotation
- Volume / media controls
- AI gesture classification

---

## 🏗️ Project Structure

```
AirMouse/
│── main.py
│── requirements.txt
│── README.md
│
├── hand_tracking/
│   └── tracker.py
│
├── mouse_control/
│   └── controller.py
│
└── utils/
    └── config.py
```

---

## ⭐ Resume-Ready Description

**Air Mouse – Gesture Controlled Virtual Mouse**  
Developed a real-time virtual mouse system using MediaPipe and OpenCV. Implemented cursor mapping, gesture recognition, dynamic smoothing, click/drag interactions, scroll control, and stability heuristics for noise-resilient human-computer interaction.

---

## 📜 License

This project is for educational and research purposes.

---

## 🙌 Acknowledgements

- MediaPipe by Google
- OpenCV Community
- PyAutoGUI
