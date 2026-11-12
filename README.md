# Skyguard

Real-time drone detection dashboard. A Python loop watches a region of the screen (for example a camera feed), runs OpenCV detection on each frame and streams the result to a browser over Socket.IO. The page lights a lamp and plays an alarm when a drone is detected.

## How it works

- `app.py` is a Flask + Flask-SocketIO server. It grabs the screen region with `mss`, processes it with OpenCV and NumPy, and emits `update` events.
- `templates/index.html` is the web UI: a status lamp and an audible alarm.

## Stack

Python, Flask, Flask-SocketIO (eventlet), OpenCV, NumPy, mss.

## Run

Needs Python 3.10 or newer.

```bash
./setup.sh              # creates .venv and installs requirements.txt
source .venv/bin/activate
./run.sh
```

Then open the address printed in the terminal.

## Tuning

`roi` (the screen region to watch) and `THRESHOLD` (detection sensitivity) are set at the top of `app.py`. Adjust both for your screen and feed.

On macOS, allow screen recording for your terminal or Python in System Settings → Privacy & Security, or `mss` will capture a blank image.
