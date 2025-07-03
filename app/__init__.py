from flask import Flask

from app.extensions import socketio


def create_app():
    SECRET_KEY = "small-potatoes"
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

    socketio.init_app(app)

    from app.routes import bp
    app.register_blueprint(bp)

    return app
