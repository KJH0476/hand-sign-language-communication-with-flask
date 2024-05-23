from flask import Blueprint, request, jsonify
from service.separate_hangul import separate_text
import variable

contents_bp = Blueprint('contents_bp', __name__)

@contents_bp.route('/text-show', methods=['POST'])
def text_show():
    data = request.get_json()
    input_word = data['text']

    result = separate_text(input_word)

    # 디버깅을 위해 추가
    print("Emitting answer event with result:", result)
    print("Emitting player_text event with text:", input_word)

    # 입력 텍스트 분리 후 언리얼 클라이언트에게 소켓 전송
    variable.socketio.emit('answer', result, namespace='/unreal')

    # 입력한 텍스트 화면에서 확인할 수 있도록 소켓 전송
    variable.socketio.emit('player_text', {'text': input_word}, namespace='/web')

    return jsonify({'status': 'success'}), 200