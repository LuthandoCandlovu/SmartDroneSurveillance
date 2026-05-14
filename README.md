# Smart Drone Surveillance System

AI-powered surveillance using YOLOv8, heatmaps, intrusion alerts, live dashboard, and real/simulated drone integration.

## Features
- Real-time human detection with YOLOv8
- Customizable intrusion zones (polygon)
- Live heatmap of movement
- GPS tracking (simulated or real Tello drone)
- Web-based dashboard with video feed, alerts, and telemetry

## Requirements
- Python 3.8+
- Webcam (or DJI Tello drone)
- See equirements.txt

## Installation

1. Clone the repo
2. Create virtual environment: python -m venv venv
3. Activate: env\Scripts\activate (Windows) or source venv/bin/activate (Linux)
4. Install packages: pip install -r requirements.txt
5. Run: python app.py
6. Open http://localhost:5000

## Usage
- Stand in front of camera → bounding box around person
- Walk into blue rectangle → intruder alert + log entry
- Heatmap builds over time
- GPS panel shows simulated circular flight (or real Tello telemetry)

## Drone Support
- Automatically detects DJI Tello (if connected to its WiFi)
- Falls back to webcam + simulated GPS

## License
MIT
