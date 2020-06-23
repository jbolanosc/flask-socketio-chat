import json
from flask import session, redirect, url_for
from flask_socketio import emit, join_room, leave_room
from util import formatMessages, get_room_users, get_current_user, get_room, user_leave

def socket_config(socketio):
    bot_name = "skynet"

    @socketio.on('join')
    def join(data):
        room = data["room"]
        join_room(room)
        users = get_room_users(str(room))

        #Welcome message
        emit('Message', formatMessages(bot_name,"Welcome to chat"))

        #Send new user connected info to others
        emit('Message', formatMessages(bot_name, data["username"] + ' has entered the room.'), room=room)

        #Send room info
        room_info = { "room": room, "users": users} 
        room_info_json = json.dumps(room_info)
        emit('roomUsers', room_info, room=room)

    @socketio.on('leave')
    def leave(data):
        room = data["room"]
        leave_room(room)
        users = user_leave(session["id"])
        print('new users')
        print(users)
        emit('Message', formatMessages(bot_name, str(session["username"]) + ' has left the room.'), room=room)
        session.clear()

        #Send room info
        room_info = { "room": room, "users": users} 
        room_info_json = json.dumps(room_info)
        emit('roomUsers', room_info, room=room)

    @socketio.on('new_message')
    def new_message(data):
        if 'id' in session:
            user = get_current_user(session["id"])
            room = int(user["room"])
            text = data
            emit('Message', formatMessages(user["username"],text), room=room)
