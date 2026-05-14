import cv2
import threading
import time
import numpy as np
import math
from flask import Flask, render_template, Response, jsonify
from flask_socketio import SocketIO
from detection_engine import DetectionEngine

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

engine = DetectionEngine(zone_points=np.array([[200,200],[400,200],[400,400],[200,400]]))

# ------------------------------------------------------------------
# Global variables for drone source
# ------------------------------------------------------------------
drone_source = None      # "tello" or "webcam_sim"
frame_reader = None
battery_level = 100
simulated_gps = {'lat': 37.7749, 'lon': -122.4194, 'angle': 0}
simulated_flight_time = 0

def init_drone():
    global drone_source, frame_reader, battery_level
    try:
        from djitellopy import Tello
        tello = Tello()
        tello.connect()
        print(f" Connected to Tello! Battery: {tello.get_battery()}%")
        tello.streamon()
        frame_reader = tello.get_frame_read()
        drone_source = "tello"
        battery_level = tello.get_battery()

        # Battery monitor thread
        def monitor_bat():
            nonlocal tello
            while True:
                if drone_source == "tello":
                    battery_level = tello.get_battery()
                time.sleep(5)
        threading.Thread(target=monitor_bat, daemon=True).start()
        return True
    except Exception as e:
        print(f"Tello connection failed: {e}")
        print("Falling back to webcam + simulated drone telemetry...")
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print(" Webcam also failed! Using blank frames.")
            cap = None
        frame_reader = cap
        drone_source = "webcam_sim"
        return False

# Start drone init (non-blocking)
init_drone()

# Simulate GPS for webcam mode
def update_simulated_gps():
    global simulated_gps, simulated_flight_time
    while drone_source == "webcam_sim":
        simulated_flight_time += 0.5
        radius = 0.002
        simulated_gps['lat'] = 37.7749 + radius * math.sin(simulated_flight_time * 0.3)
        simulated_gps['lon'] = -122.4194 + radius * math.cos(simulated_flight_time * 0.5)
        time.sleep(1)
threading.Thread(target=update_simulated_gps, daemon=True).start()

# ------------------------------------------------------------------
# Frame capture and processing
# ------------------------------------------------------------------
current_frame = None
frame_lock = threading.Lock()

def capture_and_process():
    global current_frame, drone_source, frame_reader, battery_level
    while True:
        if drone_source == "tello":
            frame = frame_reader.frame
            if frame is None:
                time.sleep(0.01)
                continue
        elif drone_source == "webcam_sim":
            if frame_reader is None:
                frame = np.zeros((480,640,3), dtype=np.uint8)
                cv2.putText(frame, "No webcam detected", (50,240), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            else:
                ret, frame = frame_reader.read()
                if not ret:
                    time.sleep(0.01)
                    continue
        else:
            time.sleep(0.1)
            continue

        processed_frame, _ = engine.process_frame(frame)
        with frame_lock:
            current_frame = processed_frame.copy()
        time.sleep(0.033)

threading.Thread(target=capture_and_process, daemon=True).start()

# ------------------------------------------------------------------
# Flask routes
# ------------------------------------------------------------------
@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/video_feed')
def video_feed():
    def generate():
        while True:
            with frame_lock:
                if current_frame is None:
                    continue
                ret, buffer = cv2.imencode('.jpg', current_frame)
                if not ret:
                    continue
                frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')
            time.sleep(0.05)
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/heatmap')
def heatmap():
    heat_img = engine.get_heatmap_image()
    ret, buffer = cv2.imencode('.jpg', heat_img)
    return Response(buffer.tobytes(), mimetype='image/jpeg')

@app.route('/alerts')
def alerts():
    recent = engine.get_recent_alerts(20)
    return jsonify([{'time': t, 'msg': m} for t,m in recent])

@app.route('/gps')
def gps_pos():
    if drone_source == "tello":
        # Tello doesn't have GPS, return simulated path for consistency
        return jsonify({'lat': 37.7749, 'lon': -122.4194, 'source': 'simulated'})
    else:
        return jsonify({'lat': simulated_gps['lat'], 'lon': simulated_gps['lon'], 'source': 'webcam_sim'})

@app.route('/status')
def status():
    if drone_source == "tello":
        return jsonify({'drone': 'real_tello', 'battery': battery_level})
    else:
        return jsonify({'drone': 'simulated_webcam', 'battery': 100})

if __name__ == '__main__':
    print(" Smart Drone Surveillance System")
    print(f" Source: {drone_source}")
    print(" Dashboard: http://localhost:5000")
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)