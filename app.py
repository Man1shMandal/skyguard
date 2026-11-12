from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import mss
import cv2
import numpy as np
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# UPDATE these values after you take a screenshot
roi = {"top": 200, "left": 300, "width": 800, "height": 300}
sct = mss.mss()

THRESHOLD = 6000  # Tune this after testing

def detect_loop():
    while True:
        frame = np.array(sct.grab(roi))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
        col_sum = np.sum(thresh, axis=0)

        peak_value = int(np.max(col_sum))
        detected = peak_value > THRESHOLD

        socketio.emit("update", {
            "detected": detected,
            "peak_value": peak_value
        })

        time.sleep(0.1)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    threading.Thread(target=detect_loop, daemon=True).start()
    socketio.run(app, host="127.0.0.1", port=5000)