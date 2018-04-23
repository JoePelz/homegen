from typing import List
from app.rooms.base_room import BaseRoom
from app import constraints


class Hallway(BaseRoom):
    def default_constraints(self) -> List["BaseConstraint"]:
        rules = [
            *BaseRoom.default_constraints(self),
            constraints.InitialSize(min_depth=43, max_depth=360, min_width=43, max_width=43),
        ]
        return rules

    def __init__(self):
        super().__init__()
        self.template = 'hallway'  # type: str
