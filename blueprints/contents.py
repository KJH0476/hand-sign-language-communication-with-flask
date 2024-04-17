from flask import Blueprint, request, jsonify
from service.separate_hangul import separate_text
import variable

contents_bp = Blueprint('contents_bp', __name__)

@contents_bp.route('/text-show', methods=['POST'])
def text_show():
    data = request.get_json()
    input_word = data['text']

    print('input word:', input_word)

    result = separate_text(input_word)
    print(result)

    #입력한 텍스트 화면에서 확인할 수 있도록 소켓 전송
    variable.socketio.emit('player_text', {'text': input_word})

    return jsonify({'status': 'success'}), 200