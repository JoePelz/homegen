from typing import List
from app.rooms.base_room import BaseRoom
from app.edge import Edge
from app import constraints


class BaseWall(BaseRoom):
    def default_constraints(self) -> List["BaseConstraint"]:
        rules = [
            *BaseRoom.default_constraints(self),
            constraints.InitialSize(min_depth=5, max_depth=5, min_width=5),
        ]
        return rules

    def __init__(self):
        super().__init__()
        self.template = 'base_wall'  # type: str

    def get_attachment_points(self) -> List[Edge]:
        return self.edges[2:3]