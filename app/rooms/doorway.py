from typing import List
from app.rooms.base_wall import BaseWall
from app import constraints


class Doorway(BaseWall):
    def default_constraints(self) -> List["BaseConstraint"]:
        rules = [
            *BaseWall.default_constraints(self),
            constraints.InitialSize(min_width=43, max_width=43),
        ]
        return rules

    def __init__(self):
        super().__init__()
        self.template = 'doorway'  # type: str
