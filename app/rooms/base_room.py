from typing import List, Tuple
from app.edge import Edge


class BaseRoom:
    MIN_WIDTH = 24
    MIN_DEPTH = 24
    MAX_WIDTH = 300
    MAX_DEPTH = 300

    def __init__(self):
        self.edges = []  # type: List[Edge]
        self.base_edge = 0  # type: int
        self.square_inches = 0.  # type: float
        self.ratio = 0.  # type: float
        self.name = ""  # type: str
        self.template = 'base'  # type: str

        x_axis = (1, 0)
        y_axis = (0, 1)
        pos = (0, 0)
        self.__transform = (0.,)*9  # type: Tuple[float, float, float, float, float, float, float, float, float]
        self.transform = (*x_axis, pos[0],
                          *y_axis, pos[1],
                          0,  0,  1)

    @property
    def transform(self) -> Tuple[float, float, float, float, float, float, float, float, float]:
        return self.__transform

    @transform.setter
    def transform(self, value: Tuple[float, float, float, float, float, float, float, float, float]) -> None:
        xx, xy, p1, yx, yy, p2, *_ = value
        xlen = (xx**2 + xy**2)**0.5
        ylen = (yx**2 + yy**2)**0.5
        xx /= xlen
        xy /= xlen
        yx /= ylen
        yy /= ylen
        self.__transform = (xx, xy, p1,
                          yx, yy, p2,
                           0,  0,  1)

    def get_ranges(self) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        return (self.MIN_WIDTH, self.MAX_WIDTH), (self.MIN_DEPTH, self.MAX_DEPTH)

    def set_box(self, width, depth) -> None:
        e1 = Edge(-width/2, 0, width/2, 0)
        e2 = Edge(*e1.end, width/2, depth)
        e3 = Edge(*e2.end, -width/2, depth)
        e4 = Edge(*e3.end, *e1.start)
        self.edges = [e1, e2, e3, e4]

    def set_transform(self, x_axis: tuple, position: tuple) -> None:
        xx, xy = x_axis
        yx, yy = -xy, xx
        self.transform = xx, xy, position[0], yx, yy, position[1]

    def get_origin(self) -> Tuple[float, float]:
        # origin = tuple(self.__transform[2:6:3])  # same as below
        return self.__transform[2], self.__transform[5]

    def get_attachment_points(self) -> List[Edge]:
        return self.edges[1:]

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
            area = round(self.square_inches / 144)
        )
        return response