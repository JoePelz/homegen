from app import constraints

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app import rooms


class Wall(constraints.BaseConstraint):
    def apply_to_room(self, room: "rooms.BaseRoom"):
        room.wall = True

    def __str__(self):
        return "Treat as a wall"
