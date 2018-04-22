from typing import List
from app.edge import Edge
from app.rooms.base_room import BaseRoom


class Closet(BaseRoom):
    MIN_WIDTH = 36
    MIN_DEPTH = 24

    MAX_WIDTH = 60
    MAX_DEPTH = 36

    def __init__(self):
        super().__init__()
        self.template = 'closet'  # type: str
