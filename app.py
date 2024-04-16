from flask import Flask
from flask_socketio import SocketIO
from blueprints.camera import camera_bp
from blueprints.web import web_bp
from blueprints.contents import contents_bp
import variable

app = Flask(__name__)
variable.socketio = SocketIO(app, logger=True, engineio_logger=True, cors_allowed_origins="*")

app.register_blueprint(camera_bp)
app.register_blueprint(web_bp)
app.register_blueprint(contents_bp)

if __name__ == '__main__':
    variable.socketio.run(app)
