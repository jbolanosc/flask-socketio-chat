import os
from flask import Flask
from routes import generate_routes
from flask_socketio import SocketIO
from events import socket_config

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


if __name__ == '__main__':
    socketio.run(app)

generate_routes(app)

socket_config(socketio)
