from typing import List
from app.rooms import BaseRoom, BaseWall
from app.transform import Transform2D
import svgwrite
# https://svgwrite.readthedocs.io/en/master/


class Blueprint:
    def __init__(self, path:str="blueprints_bkp.svg"):
        self.path = path  # type: str
        # scale is how many user units per inch
        self.scale = 1.0  # type: float
        self.dwg = svgwrite.Drawing(self.path)
        self.dwg.viewbox(-300, -200, 600, 600)
        self.colors = ['blue', 'green', 'red', 'yellow', 'white']
        self.color_index = 0

    def add_model(self, model: BaseRoom) -> None:
        if isinstance(model, BaseWall):
            self.render_wall(model)
        else:
            self.render_room(model)

    def export(self) -> None:
        self.dwg.add(self.dwg.circle((0, 0), r=10, fill='white'))
        self.dwg.save(pretty=True)

    def render_room(self, model: BaseRoom) -> None:
        points = map(lambda m: m.start, model.edges)
        matrix = Blueprint.transform_to_svg(model.transform)
        polygon = self.dwg.polygon(
            points,
            fill=self.colors[self.color_index % len(self.colors)],
            fill_opacity=0.5,
            stroke=self.colors[self.color_index % len(self.colors)],
            stroke_width=2,
            stroke_linejoin='bevel'
        )
        self.color_index += 1
        # print("model: {}".format(model.report()))
        # print(" X: {:6} {:6}".format(*matrix[0:2]))
        # print(" Y: {:6} {:6}".format(*matrix[2:4]))
        # print(" P: {:6} {:6}".format(*matrix[4:6]))
        polygon.matrix(*matrix)
        self.dwg.add(polygon)

    def render_wall(self, model: BaseWall) -> None:
        points = map(lambda m: m.start, model.edges)
        matrix = Blueprint.transform_to_svg(model.transform)
        polygon = self.dwg.polygon(
            points,
            fill='none',
            stroke='black',
            stroke_width=2,
            stroke_linejoin='bevel'
        )
        polygon.matrix(*matrix)
        self.dwg.add(polygon)

    @staticmethod
    def transform_to_svg(transform: Transform2D) -> List[float]:
        index_order = 0, 1, 2, 3, 4, 5
        matrix = [transform.values[i] for i in index_order]
        return matrix

# Polyline.__init__(points=[], **extra)
# Parameters:
# points (iterable) – iterable of points (points are 2-tuples)
# extra – additional SVG attributs as keyword-arguments
