from flask import Flask
from flask_socketio import SocketIO
import os

socketio = SocketIO()


def create_app(debug=False):
    """Create an application."""

    # SETTING THE ENV VARIABLES
    os.environ['HOST'] = '192.168.1.9'
    os.environ['PORT'] = '5000'
    os.environ['SECRET_KEY'] = 'gjr39dkjn344_!67#'



    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app
