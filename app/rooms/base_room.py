from typing import List, Tuple
from app.edge import Edge
from app.transform import Transform2D


class BaseRoom:
    def __init__(self):
        self.edges = []  # type: List[Edge]
        self.base_edge = 0  # type: int
        self.square_inches = 0.  # type: float
        self.ratio = 0.  # type: float
        self.name = ""  # type: str
        self.id = ""  # type: str
        self.template = 'base'  # type: str
        self.transform = Transform2D.identity()  # type: Transform2D

        for constraint in self.default_constraints():
            self.apply_constraint(constraint)

    def apply_constraint(self, constraint: "BaseConstraint"):
        # print("before: ({})".format(self.name))
        # print("  {}".format(self.get_ranges()))
        constraint.apply(self)
        # print("after: ")
        # print("  {}".format(self.get_ranges()))
        # print("---")

    def get_ranges(self) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        return (self.MIN_WIDTH, self.MAX_WIDTH), (self.MIN_DEPTH, self.MAX_DEPTH)

    def set_box(self, width, depth) -> None:
        e0 = Edge(-width/2, 0, width/2, 0)
        e1 = Edge(*e0.end, width/2, depth)
        e2 = Edge(*e1.end, -width/2, depth)
        e3 = Edge(*e2.end, *e0.start)
        self.edges = [e0, e1, e2, e3]
        e0.mark_used()

    def get_attachment_points(self) -> List[Edge]:
        return [e for e in self.edges if not e.used]

    def set_square_inches(self, area: float) -> None:
        self.square_inches = area

    def set_ratio(self, ratio: float) -> None:
        self.ratio = ratio

    def get_width(self) -> float:
        minx = 0
        maxx = 0
        for edge in self.edges:
            x1, y1 = edge.start
            x2, y2 = edge.end
            minx = min(minx, x1, x2)
            maxx = max(maxx, x1, x2)
        return maxx - minx

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
            name = self.name,
            template = self.template,
            width = BaseRoom.nice_feet(self.get_width()),
            height = BaseRoom.nice_feet(self.get_height()),
            # width = round(self.get_width()),
            # height = round(self.get_height()),
            area = round(self.square_inches / 144)
        )
        return response