from app import constraints

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app import rooms
    from app import meta_room


class DeadEnd(constraints.BaseConstraint):
    def apply_to_room(self, room: "rooms.BaseRoom"):
        room.dead_end = True
        room.get_attachment_points = lambda: []

    def apply_to_meta_room(self, room: "meta_room.MetaRoom"):
        room.dead_end = True

    def __str__(self):
        return "Dead end room"
