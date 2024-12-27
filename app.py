from flask import Flask, jsonify, send_from_directory, abort
import os
import random

app = Flask(__name__)

# Base directory for images
BASE_DIR = os.path.join(app.root_path, 'static', 'wallpapers')

# List of months
MONTHS = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]

# Supported devices
DEVICES = ["desktop", "laptop", "tablet", "watch"]

def find_image_path(month, device):
    """Helper function to find an image path with supported extensions."""
    for ext in ["jpg", "png"]:
        path = os.path.join(BASE_DIR, month, f"{device}.{ext}")
        if os.path.exists(path):
            return path
    return None

@app.route('/months', methods=['GET'])
def get_months():
    """Endpoint to get a list of available months."""
    return jsonify(MONTHS)

@app.route('/random-<device>', methods=['GET'])
def get_random_image(device):
    """Endpoint to get a random image for a specific device."""
    if device not in DEVICES:
        abort(404, description=f"Device '{device}' not supported.")
    
    month = random.choice(MONTHS)
    image_path = find_image_path(month, device)
    
    if image_path:
        return send_from_directory(os.path.dirname(image_path), os.path.basename(image_path))
    else:
        abort(404, description=f"No image found for {device} in {month}.")

@app.route('/<month>/<device>', methods=['GET'])
def get_specific_image(month, device):
    """Endpoint to get a specific image for a month and device."""
    if month not in MONTHS:
        abort(404, description=f"Month '{month}' not recognized.")
    if device not in DEVICES:
        abort(404, description=f"Device '{device}' not supported.")
    
    image_path = find_image_path(month, device)
    
    if image_path:
        return send_from_directory(os.path.dirname(image_path), os.path.basename(image_path))
    else:
        abort(404, description=f"No image found for {device} in {month}.")

@app.route('/random', methods=['GET'])
def get_random_image_any():
    """Endpoint to get a random image from any month and device."""
    while True:
        month = random.choice(MONTHS)
        device = random.choice(DEVICES)
        image_path = find_image_path(month, device)
        
        if image_path:
            return send_from_directory(os.path.dirname(image_path), os.path.basename(image_path))

if __name__ == '__main__':
    app.run(debug=True)
