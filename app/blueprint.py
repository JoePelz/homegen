from typing import List
from app.rooms import BaseRoom, BaseWall
from app.transform import Transform2D
import svgwrite
import svgwrite.container
# https://svgwrite.readthedocs.io/en/master/


class Blueprint:
    def __init__(self, path:str="blueprints_bkp.svg"):
        self.path = path  # type: str
        # scale is how many user units per inch
        self.scale = 1.0  # type: float
        self.dwg = svgwrite.Drawing(self.path)
        self.dwg.viewbox(-300, -200, 600, 600)
        self.dwg.defs.add(self.dwg.style(self.__class__.stylesheet()))

        self.colors = ['blue', 'green', 'red', 'yellow', 'brown', 'orange', 'teal', 'pink']
        self.color_index = 0

    @staticmethod
    def stylesheet() -> str:
        css = """
.room {
  fill-opacity: 0.5;
  stroke-width: 0.1em;
  stroke-linejoin: bevel;
}

.wall {
  fill: none;
  stroke: black;
  stroke-width: 0.1em;
  stroke-linejoin: bevel;
}

.label {
  fill: black;
  font-family: Courier New;
  font-weight: bold;
  font-size: 1.5em;
  alignment-baseline: middle;
  text-anchor: middle;
}"""
        return css

    def add_model(self, model: BaseRoom) -> None:
        if isinstance(model, BaseWall):
            self.render_wall(model)
        else:
            self.render_room(model)

    def export(self) -> None:
        self.dwg.add(self.dwg.circle((0, 0), r=10, fill='white'))
        self.dwg.save(pretty=True)

    def render_room(self, model: BaseRoom) -> svgwrite.container.Group:
        points = list(map(lambda m: m.start, model.edges))
        matrix = Blueprint.transform_to_svg(model.transform)
        polygon = self.dwg.polygon(
            points,
            class_='room',
            fill=self.colors[self.color_index % len(self.colors)],
            stroke=self.colors[self.color_index % len(self.colors)],
        )
        self.color_index += 1

        group = self.dwg.g()
        group.matrix(*matrix)

        text_center = (
            sum(p[0] for p in points) / len(model.edges),
            sum(p[1] for p in points) / len(model.edges)
        )
        text = self.dwg.text(
            model.name,
            text_center,
            class_='label'
        )
        group.add(polygon)
        group.add(text)
        return group

    def render_wall(self, model: BaseWall) -> svgwrite.container.Group:
        points = map(lambda m: m.start, model.edges)
        matrix = self.__class__.transform_to_svg(model.transform)
        polygon = self.dwg.polygon(
            points,
            class_='wall',
        )
        group = self.dwg.g()
        group.matrix(*matrix)
        group.add(polygon)
        return group

    @staticmethod
    def transform_to_svg(transform: Transform2D) -> List[float]:
        index_order = 0, 1, 2, 3, 4, 5
        matrix = [transform.values[i] for i in index_order]
        return matrix

# Polyline.__init__(points=[], **extra)
# Parameters:
# points (iterable) – iterable of points (points are 2-tuples)
# extra – additional SVG attributs as keyword-arguments
