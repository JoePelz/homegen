from app import constraints

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app import rooms


class InitialSize(constraints.BaseConstraint):
    def __init__(self, min_width: float = None, max_width: float = None,
                 min_depth: float = None, max_depth: float = None):
        self.min_width = min_width
        self.max_width = max_width
        self.min_depth = min_depth
        self.max_depth = max_depth

    def apply_to_room(self, room: "rooms.BaseRoom"):
        if self.min_width is not None:
            room.min_width = self.min_width
        if self.max_width is not None:
            room.max_width = self.max_width
        if self.min_depth is not None:
            room.min_depth = self.min_depth
        if self.max_depth is not None:
            room.max_depth = self.max_depth
