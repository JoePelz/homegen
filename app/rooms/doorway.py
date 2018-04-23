from typing import List
from app.rooms.base_wall import BaseWall
from app import constraints


class Doorway(BaseWall):
    @classmethod
    def default_constraints(cls) -> List["BaseConstraint"]:
        rules = [
            constraints.InitialSize(min_width=43, max_width=43),
        ]
        return rules

    def __init__(self):
        super().__init__()
        self.template = 'doorway'  # type: str
