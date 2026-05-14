import cv2
import numpy as np
from ultralytics import YOLO
import time
import threading

class DetectionEngine:
    def __init__(self, model_name='yolov8n.pt', zone_points=None, heatmap_size=(640,480)):
        self.model = YOLO(model_name)
        if zone_points is None:
            self.zone_points = np.array([[200,200],[400,200],[400,400],[200,400]], dtype=np.int32)
        else:
            self.zone_points = zone_points
        self.heatmap = np.zeros(heatmap_size, dtype=np.float32)
        self.alert_log = []
        self.lock = threading.Lock()
        self.frame_count = 0

    def is_point_in_zone(self, point):
        return cv2.pointPolygonTest(self.zone_points, point, False) >= 0

    def process_frame(self, frame):
        self.frame_count += 1
        results = self.model(frame, verbose=False)[0]
        detections = []
        h, w = frame.shape[:2]
        heatmap_scaled = cv2.resize(self.heatmap, (w, h))

        for box in results.boxes:
            cls = int(box.cls[0])
            if cls == 0:  # person class
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2
                centroid = (cx, cy)
                is_intruder = self.is_point_in_zone(centroid)

                color = (0,0,255) if is_intruder else (0,255,0)
                cv2.rectangle(frame, (x1,y1), (x2,y2), color, 2)
                cv2.circle(frame, centroid, 5, (0,0,255), -1)

                if 0 <= cx < w and 0 <= cy < h:
                    heatmap_scaled[cy, cx] += 1

                if is_intruder:
                    msg = f"INTRUSION ALERT at ({cx},{cy})"
                    with self.lock:
                        self.alert_log.append((time.time(), msg))
                        if len(self.alert_log) > 50:
                            self.alert_log.pop(0)
                    cv2.putText(frame, "INTRUDER!", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

                detections.append({
                    'bbox': (x1,y1,x2,y2),
                    'centroid': centroid,
                    'is_intruder': is_intruder
                })

        with self.lock:
            self.heatmap = self.heatmap * 0.95 + cv2.resize(heatmap_scaled, self.heatmap.shape[::-1]) * 0.05

        cv2.polylines(frame, [self.zone_points], True, (255,0,0), 2)
        return frame, detections

    def get_heatmap_image(self):
        with self.lock:
            heat_norm = cv2.normalize(self.heatmap, None, 0, 255, cv2.NORM_MINMAX)
            heat_uint8 = np.uint8(heat_norm)
            heat_color = cv2.applyColorMap(heat_uint8, cv2.COLORMAP_JET)
            return heat_color

    def get_recent_alerts(self, last_n=10):
        with self.lock:
            return self.alert_log[-last_n:]