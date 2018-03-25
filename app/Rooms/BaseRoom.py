class BaseRoom:
    def __init__(self):
        self.vertices = []
        self.x_size = x_size
        self.y_size = y_size

    def offset(self, x, y):
        offset_verts = [(x0+x, y0+y) for x0, y0 in self.vertices]
        self.vertices = offset_verts

    def generate(self):
        # generate sizes that a
        pass