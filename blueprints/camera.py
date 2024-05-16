from flask import Blueprint, jsonify, Response
from service.generate_hand import generate_frames
import pickle

camera_bp = Blueprint('camera_bp', __name__)

# Load your model here
model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

# ㄷ,ㅌ,ㄹ 모델 - pickle.load(open(모델 명 변경)), model_dict['model']은 변경 X
model_dict = pickle.load(open('./modeldigut.p', 'rb'))
model_digut = model_dict['model']

model_dict = pickle.load(open('./modelsiot.p', 'rb'))
model_siot = model_dict['model']

model_dict = pickle.load(open('./modelye.p', 'rb'))
model_ye = model_dict['model']


@camera_bp.route('/video')
def video_feed():
     # 모델 추가로 generate_frames 인자 추가
    return Response(generate_frames(model, model_digut,model_siot,model_ye), mimetype='multipart/x-mixed-replace; boundary=frame')

@camera_bp.route('/set_camera', methods=['POST'])
def set_camera():
    # Implementation for setting camera
    return jsonify({'status': 'success'})
