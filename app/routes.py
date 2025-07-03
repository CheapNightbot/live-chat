from flask import Blueprint, render_template
from flask_socketio import emit

from app.extensions import socketio

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@socketio.on("send_message")
def handle_message(data):
    emit("receive_message", data, broadcast=True)
