import cv2
import threading
import time
import json
from flask import Flask, render_template, Response, jsonify
from flask_socketio import SocketIO, emit
from detection_engine import DetectionEngine
from gps_simulator import GPSSimulator
import numpy as np

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize components
engine = DetectionEngine(zone_points=np.array([[200,200],[400,200],[400,400],[200,400]]))
gps = GPSSimulator()
gps.start()

# Global frame for streaming
current_frame = None
frame_lock = threading.Lock()

def capture_and_process():
    global current_frame
    cap = cv2.VideoCapture(0)  # use webcam as drone camera
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        processed_frame, detections = engine.process_frame(frame)
        with frame_lock:
            current_frame = processed_frame.copy()
        # Send alerts via WebSocket every 2 seconds
        time.sleep(0.033)  # ~30 fps
    cap.release()

# Start background thread
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
    lat, lon = gps.get_position()
    return jsonify({'lat': lat, 'lon': lon})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)
