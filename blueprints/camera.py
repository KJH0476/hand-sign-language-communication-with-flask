from flask import Blueprint, jsonify, Response
from service.generate_hand import generate_frames
import pickle

camera_bp = Blueprint('camera_bp', __name__)

# Load your model here
model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

@camera_bp.route('/video')
def video_feed():
    return Response(generate_frames(model), mimetype='multipart/x-mixed-replace; boundary=frame')

@camera_bp.route('/set_camera', methods=['POST'])
def set_camera():
    # Implementation for setting camera
    return jsonify({'status': 'success'})
