import threading
import time
import math

class GPSSimulator:
    def __init__(self, start_lat=37.7749, start_lon=-122.4194):
        self.lat = start_lat
        self.lon = start_lon
        self.start_time = time.time()
        self.lock = threading.Lock()

    def _update_loop(self):
        while True:
            t = time.time() - self.start_time
            # Simulate a circular flight path over a farm
            radius = 0.002   # ~200 meters
            self.lat = 37.7749 + radius * math.sin(t * 0.5)
            self.lon = -122.4194 + radius * math.cos(t * 0.7)
            time.sleep(0.5)

    def start(self):
        self.thread = threading.Thread(target=self._update_loop, daemon=True)
        self.thread.start()

    def get_position(self):
        with self.lock:
            return (self.lat, self.lon)
