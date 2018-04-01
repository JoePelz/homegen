# Edge represents a straight edge bounding a room or wall
# It is also like a node in a linked list


class Edge:
    def __init__(self, x1, y1, x2, y2):
        self.next = None
        self.prev = None
        self.start = (x1, y1)
        self.end = (x2, y2)
