from random import choice
from time import sleep

from flask import Blueprint, render_template
from flask_socketio import emit

from app.extensions import socketio

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@socketio.on("send_message")
def handle_message(data):
    user_message: str = data["msg"]
    if "hi" in user_message.lower() or "hello" in user_message.lower():
        response = choice(["Hello! (^///^)", "yoho ~ ! OwO"])
    else:
        response = "Me don't know what you mean! （o´・ェ・｀o）"

    # First sending user message, then our response
    emit("receive_message", data, broadcast=True)
    sleep(1)
    emit("receive_message", {"msg": response, "system": True}, broadcast=True)
