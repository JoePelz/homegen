from typing import Tuple
# Edge represents a straight edge bounding a room or wall
# It is also like a node in a linked list


class Edge:
    def __init__(self, x1:float, y1:float, x2:float, y2:float):
        self.next = None  # type: Edge
        self.prev = None  # type: Edge
        self.start = (x1, y1)  # type: Tuple[float, float]
        self.end = (x2, y2)  # type: Tuple[float, float]

    @property
    def center(self) -> Tuple[float, float]:
        x1, y1 = self.start
        x2, y2 = self.end
        return (x1+x2) / 2, (y1+y2) / 2