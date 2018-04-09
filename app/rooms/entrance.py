from typing import List
from app.edge import Edge
from app.rooms.base_wall import BaseWall


class Entrance(BaseWall):
    MIN_WIDTH = 43
    MIN_DEPTH = 43
    MAX_WIDTH = 43
    MAX_DEPTH = 43

    def __init__(self):
        super().__init__()
        self.template = 'entrance'  # type: str

    def get_attachment_points(self) -> List[Edge]:
        # return self.edges[1:2]
        return self.edges[2:3]
