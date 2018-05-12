from app import constraints

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app import rooms


class StraightPassage(constraints.BaseConstraint):
    def apply_to_room(self, room: "rooms.BaseRoom"):
        room.get_attachment_points = lambda: [room.edges[2]]

    def __str__(self):
        return "Pass straight through only"