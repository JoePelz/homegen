from app import rooms
from app.constraints import BaseConstraint


class StraightPassage(BaseConstraint):
    def apply(self, room: rooms.BaseRoom):
        room.get_attachment_points = lambda: [room.edges[2]]
