from typing import List, Tuple
from app import edge
from app import transform
from app import constraints


class BaseRoom:
    def __init__(self):
        self.edges = []  # type: List[edge.Edge]
        self.base_edge = 0  # type: int
        self.square_inches = 0.  # type: float
        self.ratio = 0.  # type: float
        self.name = ""  # type: str
        self.id = ""  # type: str
        self.template = 'base'  # type: str
        self.transform = transform.Transform2D.identity()  # type: transform.Transform2D

        self.min_width = 24
        self.min_depth = 24
        self.max_width = 300
        self.max_depth = 300
        self.wall = False
        self.dead_end = False

    def apply_constraint(self, constraint: constraints.BaseConstraint) -> None:
        constraint.apply_to_room(self)

    def get_ranges(self) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        return (self.min_width, self.max_width), (self.min_depth, self.max_depth)

    def is_a_wall(self) -> bool:
        return self.wall

    def set_box(self, width: float, depth: float) -> None:
        e0 = edge.Edge(-width/2, 0, width/2, 0)
        e1 = edge.Edge(*e0.end, width/2, depth)
        e2 = edge.Edge(*e1.end, -width/2, depth)
        e3 = edge.Edge(*e2.end, *e0.start)
        self.edges = [e0, e1, e2, e3]
        e0.mark_used()

    def get_attachment_points(self) -> List[edge.Edge]:
        return [e for e in self.edges if not e.used]

    def set_square_inches(self, area: float) -> None:
        self.square_inches = area

    def set_ratio(self, ratio: float) -> None:
        self.ratio = ratio

    def get_width(self) -> float:
        min_x = 0
        max_x = 0
        for edge in self.edges:
            x1, y1 = edge.start
            x2, y2 = edge.end
            min_x = min(min_x, x1, x2)
            max_x = max(max_x, x1, x2)
        return max_x - min_x

    def get_height(self) -> float:
        miny = 0
        maxy = 0
        for edge in self.edges:
            x1, y1 = edge.start
            x2, y2 = edge.end
            miny = min(miny, y1, y2)
            maxy = max(maxy, y1, y2)
        return maxy - miny

    @staticmethod
    def nice_feet(inches: float) -> str:
        feet = int(inches / 12)
        inches = round(inches % 12, 1)
        return "{}'{}\"".format(feet, inches)

    def report(self) -> str:
        response = "{name}({template}) - {width}x{height} ({area} sq. ft.)".format(
            name=self.name,
            template=self.template,
            width=BaseRoom.nice_feet(self.get_width()),
            height=BaseRoom.nice_feet(self.get_height()),
            # width=round(self.get_width()),
            # height=round(self.get_height()),
            area=round(self.square_inches / 144)
        )
        return response
