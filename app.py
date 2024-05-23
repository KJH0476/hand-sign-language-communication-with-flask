from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from blueprints.camera import camera_bp
from blueprints.web import web_bp
from blueprints.contents import contents_bp
import variable

app = Flask(__name__)
CORS(app)
variable.socketio = SocketIO(app, logger=True, engineio_logger=True, cors_allowed_origins="*")

app.register_blueprint(camera_bp)
app.register_blueprint(web_bp)
app.register_blueprint(contents_bp)

@variable.socketio.on('connect', namespace='/unreal')
def handle_unreal_connect():
    print('/unreal namespace connected')

@variable.socketio.on('disconnect', namespace='/unreal')
def handle_unreal_disconnect():
    print('/unreal namespace disconnected')

@variable.socketio.on('answer', namespace='/unreal')
def handle_answer(data):
    print('Answer event received:', data)
    emit('response', {'data': 'Answer received'}, namespace='/unreal')

@variable.socketio.on('connect', namespace='/web')
def handle_web_connect():
    print('/web namespace connected')

@variable.socketio.on('disconnect', namespace='/web')
def handle_web_disconnect():
    print('/web namespace disconnected')

@variable.socketio.on('player_text', namespace='/web')
def handle_player_text(data):
    print('Player text event received:', data)
    emit('response', {'data': 'Player text received'}, namespace='/web')

if __name__ == '__main__':
    variable.socketio.run(app)
