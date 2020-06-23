rooms = [{"id": "1", "description":"JS Lovers"}, {"id": "2", "description":"Python Lovers"}]

def create_room(description):
    newRoom = { "id": str(len(rooms) + 1), "description": description}
    rooms.append(newRoom)
    return newRoom["id"]

def get_room(id):
    for room in rooms:
        if room["id"] == id:
            return room

def get_all_rooms():
    return rooms