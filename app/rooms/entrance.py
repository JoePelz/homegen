from typing import List
from app.edge import Edge
from app.rooms.base_wall import BaseWall
from app import constraints


class Entrance(BaseWall):
    def default_constraints(self) -> List["BaseConstraint"]:
        rules = [
            *BaseWall.default_constraints(self),
            constraints.InitialSize(min_depth=43, max_depth=43, min_width=43, max_width=43),
        ]
        return rules

    def __init__(self):
        super().__init__()
        self.template = 'entrance'  # type: str

    def get_attachment_points(self) -> List[Edge]:
        # return self.edges[1:2]
        if self.edges[2].used:
            return []
        else:
            return [self.edges[2]]
