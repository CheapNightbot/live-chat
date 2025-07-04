from app import create_app
from app.extensions import socketio

app = create_app()


if __name__ == "__main__":
    socketio.run(
        app=app,
        host="127.0.0.1",
        port=5000,
        debug=True,
    )
