from flask import session
users = []

def user_join(id, username, room):
    user = {"id": id,"username": username,"room": room}
    users.append(user)
    session["users"] = users
    return user

def user_leave(id):
    user = get_current_user(id)
    print(session["users"])
    print(users)
    users.remove(user)
    return users

def get_current_user(id):
    for user in users:
        if user["id"] == id:
            return user

def get_room_users(room):
    room_users = []
    for user in users:
        if user["room"] == room:
            room_users.append(user)
    
    return room_users


