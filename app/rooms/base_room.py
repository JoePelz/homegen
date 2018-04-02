from typing import List
from app.edge import Edge


class BaseRoom:
    MIN_WIDTH = 24
    MIN_DEPTH = 24
    MAX_WIDTH = 300
    MAX_DEPTH = 300

    def __init__(self):
        self.edges = []
        self.base_edge = 0

        x_axis = (1, 0)
        y_axis = (0, 1)
        pos = (0, 0)
        self.__transform = [0]*9
        self.transform = (*x_axis, pos[0],
                          *y_axis, pos[1],
                          0,  0,  1)

    @property
    def transform(self):
        return self.__transform

    @transform.setter
    def transform(self, value):
        xx, xy, p1, yx, yy, p2, _ = value
        xlen = xx**2 + yy**2
        ylen = yx**2 + yy**2
        xx /= xlen
        xy /= xlen
        yx /= ylen
        yy /= ylen
        self.__transform = (xx, xy, p1,
                          yx, yy, p2,
                           0,  0,  1)

    def get_ranges(self):
        return (self.MIN_WIDTH, self.MAX_WIDTH), (self.MIN_DEPTH, self.MAX_DEPTH)

    def set_box(self, width, depth):
        e1 = Edge(-width/2, 0, width/2, 0)
        e2 = Edge(*e1.end, width/2, depth)
        e3 = Edge(*e2.end, -width/2, depth)
        e4 = Edge(*e3.end, e1.start)
        self.edges = [e1, e2, e3, e4]

    def set_transform(self, x_axis: tuple, position: tuple):
        xx, xy = x_axis
        yx, yy = -xy, xx
        self.transform = xx, xy, position[0], yx, yy, position[1]

    def get_origin(self):
        # origin = tuple(self.__transform[2:6:3])  # same as below
        return self.__transform[2], self.__transform[5]

    def get_attachment_points(self) -> List[Edge]:
        return self.edges[1:]