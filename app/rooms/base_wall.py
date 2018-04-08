from typing import List
from app.rooms.base_room import BaseRoom
from app.edge import Edge


class BaseWall(BaseRoom):
    MIN_DEPTH = 5
    MAX_DEPTH = 5

    MIN_WIDTH = 5

    def __init__(self):
        super().__init__()
        self.template = 'base_wall'  # type: str

    def get_attachment_points(self) -> List[Edge]:
        return self.edges[2:3]