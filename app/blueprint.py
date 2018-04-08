from typing import Tuple
from app.rooms import BaseRoom
import svgwrite
# https://svgwrite.readthedocs.io/en/master/


class Blueprint:
    def __init__(self, path:str="blueprints.svg"):
        self.path = path  # type: str
        # scale is how many user units per inch
        self.scale = 1.0  # type: float
        self.dwg = svgwrite.Drawing("blueprints.svg")
        self.dwg.viewbox(-200, 0, 400, 400)
        self.colors = ['blue', 'green', 'red', 'yellow', 'white', 'black']
        self.color_index = 0

    def add_model(self, model: BaseRoom) -> None:
        points = map(lambda m: m.start, model.edges)
        matrix = Blueprint.transform_to_svg(model.transform)
        polygon = self.dwg.polygon(points, fill=self.colors[self.color_index % len(self.colors)])
        self.color_index += 1
        print("model: {}".format(model.report()))
        print("{:6} {:6} {:6}".format(*matrix[:3]))
        print("{:6} {:6} {:6}".format(*matrix[3:]))
        polygon.matrix(*matrix)
        self.dwg.add(polygon)

    def export(self):
        self.dwg.add(self.dwg.circle((0, 0), r=10, fill='white'))
        self.dwg.save(pretty=True)

    @staticmethod
    def transform_to_svg(transform: Tuple[float, float, float, float, float, float]):
        index_order = 0, 3, 1, 4, 2, 5
        return [transform[i] for i in index_order]

# Polyline.__init__(points=[], **extra)
# Parameters:
# points (iterable) – iterable of points (points are 2-tuples)
# extra – additional SVG attributs as keyword-arguments