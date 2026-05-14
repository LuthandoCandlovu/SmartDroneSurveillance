import cv2
import threading
import time
import numpy as np
from flask import Flask, render_template, Response, jsonify
from flask_socketio import SocketIO
from detection_engine import DetectionEngine
from djitellopy import Tello

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Detection engine with restricted zone
engine = DetectionEngine(zone_points=np.array([[200,200],[400,200],[400,400],[200,400]]))

# Connect to Tello drone
print("Connecting to Tello drone...")
tello = Tello()
tello.connect()
print(f"Battery: {tello.get_battery()}%")
tello.streamon()
frame_reader = tello.get_frame_read()

current_frame = None
frame_lock = threading.Lock()

def capture_and_process():
    global current_frame
    while True:
        frame = frame_reader.frame
        if frame is None:
            continue
        processed_frame, _ = engine.process_frame(frame)
        with frame_lock:
            current_frame = processed_frame.copy()
        # Optional: small delay to control CPU usage
        time.sleep(0.033)

# Start background processing
threading.Thread(target=capture_and_process, daemon=True).start()

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
    # Tello doesn't have GPS; you can replace with actual telemetry if available
    return jsonify({'lat': 37.7749, 'lon': -122.4194, 'note': 'simulated'})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)
