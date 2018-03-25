class BaseRoom:
    MIN_WIDTH = 24
    MIN_DEPTH = 24
    MAX_WIDTH = 300
    MAX_DEPTH = 300

    def __init__(self):
        self.vertices = []
        self.x_size = 0
        self.y_size = 0
        self.start_edge = None

    def get_ranges(self):
        return (self.MIN_WIDTH, self.MAX_WIDTH), (self.MIN_DEPTH, self.MAX_DEPTH)

    def offset(self, x, y):
        offset_vertices = [(x0+x, y0+y) for x0, y0 in self.vertices]
        self.vertices = offset_vertices

    def generate(self):
        pass
