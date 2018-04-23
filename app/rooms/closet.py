from typing import List
from app.rooms.base_room import BaseRoom
from app import constraints


class Closet(BaseRoom):
    @classmethod
    def default_constraints(cls) -> List["BaseConstraint"]:
        rules = [
            constraints.InitialSize(min_depth=24, max_depth=36, min_width=36, max_width=60),
            constraints.DeadEnd(),
        ]
        return rules

    def __init__(self):
        super().__init__()
        self.template = 'closet'  # type: str

