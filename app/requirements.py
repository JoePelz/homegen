from app.meta_room import MetaRoom


class Requirements:
    def __init__(self):
        self.rooms = []
        self.constraints = []

    def add_room(self, room: MetaRoom) -> None:
        self.rooms.append(room)
