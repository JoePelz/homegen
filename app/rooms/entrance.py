from typing import List
from app.edge import Edge
from app.rooms.base_wall import BaseWall


class Entrance(BaseWall):
    MIN_WIDTH = 43
    MIN_DEPTH = 43
    MAX_WIDTH = 43
    MAX_DEPTH = 43

    def get_attachment_points(self) -> List[Edge]:
        return self.edges[2:3]
