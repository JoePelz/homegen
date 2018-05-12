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

    def __str__(self):
        bounds = []
        if self.min_width is not None or self.max_width is not None:
            lower = "" if self.min_width is None else self.min_width
            upper = "" if self.max_width is None else self.max_width
            bounds.append("width: [{}..{}]".format(lower, upper))
        if self.min_depth is not None or self.max_depth is not None:
            lower = "" if self.min_depth is None else self.min_depth
            upper = "" if self.max_depth is None else self.max_depth
            bounds.append("depth: [{}..{}]".format(lower, upper))
        return "Adjust initial size: {}".format(", ".join(bounds))
