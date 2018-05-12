from typing import List
import re
from app import rooms
from app import constraints
from app import templates


class MetaRoom:
    __room_ids = {}

    def __init__(self, template: str, name: str, min_count: int=1, max_count: int=1, constraints: List[constraints.BaseConstraint]=None):
        self.template = template  # type: str
        self.constraints = templates.Templates.get_template_constraints(self.template) + (constraints or [])  # type: List[constraints.BaseConstraint]
        self.name = name  # type: str
        self.id = self.get_id(name)
        self.min_count = min_count  # type: int
        self.max_count = max_count  # type: int
        self.dead_end = False

        for constraint in self.constraints:
            constraint.apply_to_meta_room(self)

    def instantiate(self) -> rooms.BaseRoom:
        room = rooms.BaseRoom()
        for constraint in self.constraints:
            room.apply_constraint(constraint)
        room.name = self.name
        room.id = self.id
        return room

    @classmethod
    def reset_ids(cls):
        cls.__room_ids = {}

    @classmethod
    def get_id(cls, name: str) -> str:
        lower_name = name.lower()
        id_name = re.sub('[^\w]+', '_', lower_name)
        room_id = id_name
        if id_name in cls.__room_ids:
            index = cls.__room_ids[id_name] + 1
            room_id = "{}_{}".format(room_id, index)
            cls.__room_ids[id_name] = index
        else:
            cls.__room_ids[id_name] = 1
        return room_id

    def  __str__(self) -> str:
        desc = '<MetaRoom({template}) "{name}" x{min}..{max}>'.format(
            template=self.template,
            name=self.name,
            min=self.min_count,
            max=self.max_count
        )
        return desc

    def __repr__(self) -> str:
        defn = "MetaRoom(template='{template}', name='{name}', min_count={min}, max_count={max}, constraints={cnst})".format(
            template=self.template,
            name=self.name,
            min=self.min_count,
            max=self.max_count,
            cnst=self.constraints
        )
        return defn

    def dup(self) -> 'MetaRoom':
        copy = MetaRoom(
            self.template,
            self.name,
            self.min_count,
            self.max_count,
            self.constraints
        )
        return copy
