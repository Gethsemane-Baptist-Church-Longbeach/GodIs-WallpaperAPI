from flask import Flask, jsonify, send_from_directory, abort
import os
import random

app = Flask(__name__)

# ------------------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------------------
BASE_DIR = os.path.join(app.root_path, 'static', 'wallpapers')
THUMBNAILS_BASE_DIR = os.path.join(app.root_path, 'static', 'thumbnails')

MONTHS = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]
DEVICES = ["laptop", "phone", "tablet", "watch"]
ALLOWED_EXTENSIONS = ["jpg", "png"]

VALID_IMAGE_PAIRS = []
VALID_THUMBNAIL_PAIRS = []

# ------------------------------------------------------------------------------
# Helper Functions
# ------------------------------------------------------------------------------
def find_image_path(month, device):
    for ext in ALLOWED_EXTENSIONS:
        path = os.path.join(BASE_DIR, month, f"{device}.{ext}")
        if os.path.exists(path):
            return path
    return None

def find_thumbnail_path(month, device):
    for ext in ALLOWED_EXTENSIONS:
        path = os.path.join(THUMBNAILS_BASE_DIR, month, f"{device}.{ext}")
        if os.path.exists(path):
            return path
    return None

def build_valid_image_pairs():
    VALID_IMAGE_PAIRS.clear()
    for month in MONTHS:
        for device in DEVICES:
            if find_image_path(month, device):
                VALID_IMAGE_PAIRS.append((month, device))

def build_valid_thumbnail_pairs():
    VALID_THUMBNAIL_PAIRS.clear()
    for month in MONTHS:
        for device in DEVICES:
            if find_thumbnail_path(month, device):
                VALID_THUMBNAIL_PAIRS.append((month, device))

# ------------------------------------------------------------------------------
# Routes
# ------------------------------------------------------------------------------
@app.route('/months', methods=['GET'])
def get_months():
    """Return a list of all supported months."""
    return jsonify(MONTHS)

@app.route('/<month>/<device>', methods=['GET'])
def get_specific_image(month, device):
    if month not in MONTHS:
        abort(404, description=f"Month '{month}' not recognized.")
    if device not in DEVICES:
        abort(404, description=f"Device '{device}' not supported.")

    image_path = find_image_path(month, device)
    if not image_path:
        abort(404, description=f"No wallpaper found for {device} in {month}.")
    return send_from_directory(os.path.dirname(image_path), os.path.basename(image_path))

@app.route('/random-<device>', methods=['GET'])
def get_random_image_for_device(device):
    if device not in DEVICES:
        abort(404, description=f"Device '{device}' not supported.")

    device_pairs = [(m, d) for (m, d) in VALID_IMAGE_PAIRS if d == device]
    if not device_pairs:
        abort(404, description=f"No wallpapers found for device '{device}'.")

    month, device = random.choice(device_pairs)
    image_path = find_image_path(month, device)
    if not image_path:
        abort(404, description=f"No wallpaper found for {device} in {month}.")
    return send_from_directory(os.path.dirname(image_path), os.path.basename(image_path))

@app.route('/random', methods=['GET'])
def get_random_image():
    if not VALID_IMAGE_PAIRS:
        abort(404, description="No valid wallpapers found on the server.")

    month, device = random.choice(VALID_IMAGE_PAIRS)
    image_path = find_image_path(month, device)
    return send_from_directory(os.path.dirname(image_path), os.path.basename(image_path))

@app.route('/thumbnails/<month>/<device>', methods=['GET'])
def get_specific_thumbnail(month, device):
    if month not in MONTHS:
        abort(404, description=f"Month '{month}' not recognized.")
    if device not in DEVICES:
        abort(404, description=f"Device '{device}' not supported.")

    thumbnail_path = find_thumbnail_path(month, device)
    if not thumbnail_path:
        abort(404, description=f"No thumbnail found for {device} in {month}.")
    return send_from_directory(os.path.dirname(thumbnail_path), os.path.basename(thumbnail_path))

@app.route('/thumbnails/random-<device>', methods=['GET'])
def get_random_thumbnail_for_device(device):
    if device not in DEVICES:
        abort(404, description=f"Device '{device}' not supported.")

    device_pairs = [(m, d) for (m, d) in VALID_THUMBNAIL_PAIRS if d == device]
    if not device_pairs:
        abort(404, description=f"No thumbnails found for device '{device}'.")

    month, device = random.choice(device_pairs)
    thumbnail_path = find_thumbnail_path(month, device)
    if not thumbnail_path:
        abort(404, description=f"No thumbnail found for {device} in {month}.")
    return send_from_directory(os.path.dirname(thumbnail_path), os.path.basename(thumbnail_path))

@app.route('/thumbnails/random', methods=['GET'])
def get_random_thumbnail():
    if not VALID_THUMBNAIL_PAIRS:
        abort(404, description="No valid thumbnails found on the server.")

    month, device = random.choice(VALID_THUMBNAIL_PAIRS)
    thumbnail_path = find_thumbnail_path(month, device)
    return send_from_directory(os.path.dirname(thumbnail_path), os.path.basename(thumbnail_path))

# ------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    # Build valid (month, device) combos BEFORE running the app
    build_valid_image_pairs()
    build_valid_thumbnail_pairs()

    app.run(debug=True)
