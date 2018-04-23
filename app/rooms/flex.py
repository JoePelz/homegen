from typing import List
from app.rooms.base_room import BaseRoom
from app import constraints


class Flex(BaseRoom):
    @classmethod
    def default_constraints(cls) -> List["BaseConstraint"]:
        rules = [
            constraints.InitialSize(min_depth=72, max_depth=150, min_width=72, max_width=150),
        ]
        return rules

    def __init__(self):
        super().__init__()
        self.template = 'flex'  # type: str
