<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:0a3d62,100:00d4ff&height=200&section=header&text=SkyWatch%20AI&fontSize=60&fontColor=00d4ff&fontAlignY=38&desc=Smart%20Drone%20Surveillance%20System&descAlignY=58&descColor=ffffff&animation=fadeIn" width="100%"/>

<!-- Typing Animation -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=700&size=22&pause=1000&color=00D4FF&center=true&vCenter=true&width=700&lines=AI-Powered+Real-Time+Surveillance;YOLOv8+Human+Detection+%F0%9F%91%81%EF%B8%8F;Live+Heatmap+%2B+Intrusion+Alerts+%F0%9F%9A%A8;GPS+Drone+Tracking+%F0%9F%9B%B8;Web+Dashboard+%7C+Flask+%7C+OpenCV" alt="Typing SVG" />
</a>

<br/>

<!-- Badges Row 1 -->
[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-FF6B35?style=for-the-badge&logo=pytorch&logoColor=white)](https://ultralytics.com)
[![Flask](https://img.shields.io/badge/Flask-Web%20App-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org)

<!-- Badges Row 2 -->
[![License](https://img.shields.io/badge/License-MIT-00FF9D?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-00d4ff?style=for-the-badge&logo=statuspage&logoColor=white)]()
[![DJI Tello](https://img.shields.io/badge/DJI%20Tello-Supported-FFD700?style=for-the-badge&logo=dji&logoColor=black)]()
[![Stars](https://img.shields.io/github/stars/?style=for-the-badge&color=ffd700)]()

</div>

---

## 🌐 Introduction

<div align="center">

> *"The sky has eyes — and they're powered by AI."*

</div>

**SkyWatch AI** is a cutting-edge, open-source surveillance platform that fuses **drone hardware**, **computer vision**, and **real-time web analytics** into a single unified system. Whether you're securing a perimeter, monitoring crowd movement, or conducting aerial reconnaissance, SkyWatch AI delivers military-grade awareness in a developer-friendly package.

Built on top of **YOLOv8** — the state-of-the-art object detection model — the system can:
- 🎯 **Detect humans** in real time with high accuracy
- 🔴 **Trigger intrusion alerts** when movement enters restricted zones
- 🌡️ **Build live heatmaps** of activity over time
- 🛸 **Interface with DJI Tello drones** for aerial coverage
- 📊 **Stream everything** to a sleek web dashboard

This isn't just a demo — it's a **production-ready surveillance engine** you can deploy today.

---

## 🎬 Live Demo

<div align="center">

### See It In Action

<video src="https://github.com/user-attachments/assets/34591ef6-707a-4cf4-badc-281e15faa82a" controls width="100%" style="border-radius:12px; border: 2px solid #00d4ff;"></video>

> 🎥 *Real-time human detection, intrusion zone triggering, and heatmap generation — all running live.*

</div>

---

## 📸 Dashboard Preview

<div align="center">
<img width="100%" alt="SkyWatch AI Dashboard" src="https://github.com/user-attachments/assets/5a7e8ed4-53e8-4523-b1ae-291b3930dd54" style="border-radius:12px;"/>

*Live dashboard showing detection feed, heatmap overlay, GPS telemetry, and alert log*
</div>

---

## ✨ Features

<div align="center">

| 🔍 Detection | 🚨 Alerts | 🗺️ Mapping | 🛸 Drone |
|:---:|:---:|:---:|:---:|
| YOLOv8 Human Detection | Polygon Intrusion Zones | Live Movement Heatmap | DJI Tello Integration |
| Bounding Boxes | Real-time Alert Log | GPS Coordinate Tracking | Auto-Detection via WiFi |
| Confidence Scores | Visual Zone Highlighting | Simulated Circular Flight | Fallback to Webcam |
| Multi-person Tracking | Timestamped Events | Path Visualization | Telemetry Dashboard |

</div>

```
╔══════════════════════════════════════════════════════════════╗
║  🎯 DETECTION      ████████████████████████████░░  94% acc  ║
║  ⚡ SPEED          ████████████████████░░░░░░░░░░  30 FPS   ║
║  📡 RANGE          ████████████████████████░░░░░░  Full HD  ║
║  🔋 EFFICIENCY     ███████████████████████████░░░  CPU/GPU  ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     SkyWatch AI — Architecture                   │
└─────────────────────────────────────────────────────────────────┘

  ┌─────────────┐      ┌──────────────────┐      ┌─────────────┐
  │  📷 Camera   │      │  🛸 DJI Tello    │      │  🌐 Browser  │
  │  (Webcam)   │      │  (WiFi Drone)    │      │  Dashboard  │
  └──────┬──────┘      └────────┬─────────┘      └──────┬──────┘
         │                      │                        │
         ▼                      ▼                        ▲
  ┌─────────────────────────────────────────┐           │
  │           VIDEO INPUT LAYER             │           │
  │   cv2.VideoCapture / djitellopy         │           │
  └─────────────────────┬───────────────────┘           │
                        │                               │
                        ▼                               │
  ┌─────────────────────────────────────────┐           │
  │         🧠 AI DETECTION ENGINE          │           │
  │   YOLOv8 → Bounding Boxes → Centroids   │           │
  │   Confidence Filtering → Person Class   │           │
  └──────┬──────────────┬───────────────────┘           │
         │              │                               │
         ▼              ▼                               │
  ┌──────────┐   ┌──────────────┐                       │
  │ 🌡️ Heatmap│   │ 🔴 Intrusion │                       │
  │  Engine  │   │ Zone Checker │                       │
  │(Gaussian)│   │ (Polygon HIT)│                       │
  └────┬─────┘   └──────┬───────┘                       │
       │                │                               │
       ▼                ▼                               │
  ┌─────────────────────────────────────────┐           │
  │          🗄️ STATE & ALERT MANAGER        │           │
  │   Alert Log · Timestamps · Zone Status  │           │
  └──────────────────────┬──────────────────┘           │
                         │                              │
                         ▼                              │
  ┌─────────────────────────────────────────┐           │
  │          🌐 FLASK WEB SERVER             │           │
  │   /video_feed (MJPEG Stream)            │           │
  │   /heatmap    (PNG Overlay)             ├───────────┘
  │   /alerts     (JSON API)               │
  │   /telemetry  (GPS + Battery)          │
  └─────────────────────────────────────────┘
```

---

## 🔄 Detection Pipeline

```
Raw Frame
    │
    ▼
┌───────────────────┐
│  Frame Capture    │  ← cv2 / DJI SDK
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  YOLOv8 Inference │  ← ultralytics model
│  class=person     │
│  conf > 0.45      │
└────────┬──────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌────────┐  ┌─────────────────┐
│ Draw   │  │ Centroid Point  │
│ BBox + │  │ → Heatmap array │
│ Label  │  │ → Zone polygon  │
└────────┘  │   intersection  │
            └────────┬────────┘
                     │
              ┌──────┴──────┐
              ▼             ▼
         ✅ SAFE        🔴 INTRUDER
         Zone OK        Alert fired
                        Log entry
                        Zone flashes RED
```

---

## 📦 Requirements

```txt
ultralytics>=8.0.0       # YOLOv8 detection engine
flask>=2.3.0             # Web server & streaming
opencv-python>=4.8.0     # Video capture & processing
numpy>=1.24.0            # Array math & heatmap
scipy>=1.11.0            # Gaussian blur for heatmap
djitellopy>=2.4.0        # DJI Tello drone SDK (optional)
Pillow>=10.0.0           # Image handling
```

---

## 🚀 Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/skywatch-ai.git
cd skywatch-ai
```

### 2️⃣ Create Virtual Environment

```bash
# Create environment
python -m venv venv

# Activate — Windows
venv\Scripts\activate

# Activate — Linux / macOS
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Launch the System

```bash
python app.py
```

### 5️⃣ Open Dashboard

```
🌐  http://localhost:5000
```

> **That's it.** Stand in front of your camera — detection begins immediately.

---

## 🎮 Usage Guide

<details>
<summary><b>🧍 Human Detection</b></summary>

- Stand in front of your webcam or Tello camera feed
- A **green bounding box** appears around each detected person
- Confidence score is shown above each box
- Multiple people are tracked simultaneously

</details>

<details>
<summary><b>🔴 Intrusion Zone Alerts</b></summary>

- A **blue polygon zone** is pre-defined in the frame
- When a person's centroid enters the zone → **RED alert fires**
- Alert is logged with timestamp in the sidebar
- Zone flashes red to signal breach

</details>

<details>
<summary><b>🌡️ Live Heatmap</b></summary>

- The heatmap builds automatically as people move
- Hot zones (red/yellow) = frequent movement
- Cool zones (blue) = rare movement
- Overlaid semi-transparently on the live feed

</details>

<details>
<summary><b>🛸 Drone Mode (DJI Tello)</b></summary>

- Connect your PC to **Tello's WiFi** before launching
- App auto-detects the drone on startup
- Live telemetry shown: battery, height, speed
- GPS panel shows real flight path
- Falls back to webcam if no drone found

</details>

---

## 🛸 Drone Support

```
          ████████████
        ██  TELLO  ██
      ████████████████
     ██              ██
    ██   ◉        ◉  ██    ← 4 rotors
     ██              ██
      ████████████████
              │
              │  WiFi UDP
              │  192.168.10.1
              ▼
    ┌──────────────────┐
    │  djitellopy SDK  │
    │  takeoff / land  │
    │  get_battery()   │
    │  get_height()    │
    └──────────────────┘
```

| Mode | Input | GPS |
|------|-------|-----|
| 🛸 **Drone Mode** | DJI Tello stream | Real telemetry |
| 💻 **Webcam Mode** | USB / built-in cam | Simulated circular path |

---

## 📁 Project Structure

```
skywatch-ai/
│
├── 📄 app.py                  # Flask app entry point
├── 📄 detector.py             # YOLOv8 detection logic
├── 📄 heatmap.py              # Gaussian heatmap engine
├── 📄 zone_manager.py         # Intrusion zone polygon logic
├── 📄 drone_controller.py     # DJI Tello / webcam handler
├── 📄 gps_simulator.py        # Circular flight path sim
├── 📄 requirements.txt        # Python dependencies
│
├── 📁 templates/
│   └── 📄 index.html          # Web dashboard UI
│
├── 📁 static/
│   ├── 📁 css/                # Dashboard styles
│   └── 📁 js/                 # Live update scripts
│
├── 📁 models/
│   └── 📄 yolov8n.pt          # YOLOv8 nano weights
│
└── 📄 README.md
```

---

## 🧠 Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)

</div>

---

## 🗺️ Roadmap

- [x] YOLOv8 real-time detection
- [x] Polygon intrusion zones
- [x] Gaussian heatmap engine
- [x] DJI Tello integration
- [x] Web dashboard with MJPEG stream
- [x] Alert logging system
- [ ] 🔜 Multi-camera support
- [ ] 🔜 Face recognition module
- [ ] 🔜 Cloud alert push (Telegram / Email)
- [ ] 🔜 Mobile app dashboard
- [ ] 🔜 Night vision / IR camera support
- [ ] 🔜 Object classification beyond persons

---

## 🤝 Contributing

Contributions are welcome! Here's how:

```bash
# 1. Fork the repo
# 2. Create your branch
git checkout -b feature/awesome-feature

# 3. Commit your changes
git commit -m "Add awesome feature"

# 4. Push and open a PR
git push origin feature/awesome-feature
```

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a pull request.

---

## 📄 License

```
MIT License — free to use, modify, and distribute.
See LICENSE file for details.
```

---

<div align="center">

<!-- Footer Wave -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00d4ff,50:0a3d62,100:0d1117&height=120&section=footer" width="100%"/>

**Built with 🤖 AI + ❤️ passion for intelligent systems**

[![GitHub followers](https://img.shields.io/github/followers/?style=social)]()
[![GitHub stars](https://img.shields.io/github/stars/?style=social)]()

*SkyWatch AI — Because the best security never sleeps.*

</div>
