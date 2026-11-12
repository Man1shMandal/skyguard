#!/usr/bin/env bash
set -euo pipefail

# Create a virtual environment and install dependencies
PYTHON=${PYTHON:-python3}

if ! command -v "$PYTHON" >/dev/null 2>&1; then
  echo "$PYTHON not found. Please install Python 3.x and try again." >&2
  exit 1
fi

echo "Creating virtual environment in .venv..."
$PYTHON -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete. Activate with: source .venv/bin/activate"
echo "Run the app with: ./run.sh"
#!/usr/bin/env bash
set -e

# Create venv in project folder and install dependencies
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "Virtual environment created and dependencies installed. Activate with: source .venv/bin/activate"