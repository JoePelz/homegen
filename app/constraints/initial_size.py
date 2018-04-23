from app import rooms
from app.constraints import BaseConstraint


class InitialSize(BaseConstraint):
    def __init__(self, min_width: float = None, max_width: float = None,
                 min_depth: float = None, max_depth: float = None):
        self.min_width = min_width
        self.max_width = max_width
        self.min_depth = min_depth
        self.max_depth = max_depth

    def apply(self, room: rooms.BaseRoom):
        if self.min_width is not None:
            room.MIN_WIDTH = self.min_width
        if self.max_width is not None:
            room.MAX_WIDTH = self.max_width
        if self.min_depth is not None:
            room.MIN_DEPTH = self.min_depth
        if self.max_depth is not None:
            room.MAX_DEPTH = self.max_depth
