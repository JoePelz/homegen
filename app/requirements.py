from typing import List
from app.meta_room import MetaRoom


class Requirements:
    def __init__(self):
        self.rooms = []  # type: List[MetaRoom]
        self.constraints = []  # type: list

    def add_room(self, room: MetaRoom) -> None:
        self.rooms.append(room)

    def room_report(self):
        fewest = sum(map(lambda x: x.min_count, self.rooms))
        most = sum(map(lambda x: x.max_count, self.rooms))
        if fewest == most:
            print("{} Rooms:".format(fewest))
        else:
            print("{}-{} Rooms:".format(fewest, most))
        for room in self.rooms:
            if room.min_count == room.max_count:
                print("  {}({}) x{}".format(room.name, room.template, room.min_count))
            else:
                print("  {}({}) x{}-{}".format(room.name, room.template, room.min_count, room.max_count))
