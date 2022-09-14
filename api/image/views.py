from flask import Blueprint, jsonify, request
from .helpers import handle_upload_image
from flasgger import swag_from


image = Blueprint('image', __name__)

@image.route('/upload', methods=['POST'])
@swag_from("./docs/upload.yml", endpoint='image.upload_image', methods=['POST'])
def upload_image():
    """Upload an image."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file has been uploaded'})
    return handle_upload_image(request.files['file'])