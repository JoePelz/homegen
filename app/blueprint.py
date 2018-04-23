from typing import List
from app.rooms import BaseRoom, BaseWall
from app.transform import Transform2D
import svgwrite
import svgwrite.container
# https://svgwrite.readthedocs.io/en/master/


class Blueprint:
    def __init__(self, path:str="blueprints.svg"):
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
            element = self.render_wall(model)
        else:
            element = self.render_room(model)
        self.dwg.add(element)

    def export(self) -> None:
        self.dwg.add(self.dwg.circle((0, 0), r=10, fill='white'))
        self.resize_viewbox()
        self.dwg.save(pretty=True)

    def resize_viewbox(self, margin: float=30) -> None:
        # traverse
        tree = self.dwg.get_xml()

        min_x = -250
        max_x = 250
        min_y = 0
        max_y = 500
        self.dwg.viewbox(
            min_x - margin,
            min_y - margin,
            (max_x - min_x) + 2 * margin,
            (max_y - min_y) + 2 * margin)

    def group(self, *elements: List[svgwrite.container.BaseElement], matrix: Transform2D=None, room_id: str=''):
        if room_id:
            group = self.dwg.g(id=room_id)
        else:
            group = self.dwg.g()
        if matrix:
            group.matrix(*self.__class__.transform_to_svg(matrix))
        for element in elements:
            group.add(element)
        return group

    def render_room(self, model: BaseRoom) -> svgwrite.container.Group:
        points = list(map(lambda m: m.start, model.edges))
        polygon = self.dwg.polygon(
            points,
            class_='room',
            fill=self.colors[self.color_index % len(self.colors)],
            stroke=self.colors[self.color_index % len(self.colors)],
        )
        self.color_index += 1

        text_center = (
            sum(p[0] for p in points) / len(model.edges),
            sum(p[1] for p in points) / len(model.edges)
        )
        text = self.dwg.text(
            model.name,
            text_center,
            class_='label'
        )
        return self.group(polygon, text, room_id=model.id, matrix=model.transform)

    def render_wall(self, model: BaseWall) -> svgwrite.container.Group:
        points = map(lambda m: m.start, model.edges)
        matrix = self.__class__.transform_to_svg(model.transform)
        polygon = self.dwg.polygon(
            points,
            class_='wall',
        )
        return self.group(polygon, room_id=model.id, matrix=model.transform)

    @staticmethod
    def transform_to_svg(transform: Transform2D) -> List[float]:
        index_order = 0, 1, 2, 3, 4, 5
        matrix = [transform.values[i] for i in index_order]
        return matrix

# Polyline.__init__(points=[], **extra)
# Parameters:
# points (iterable) – iterable of points (points are 2-tuples)
# extra – additional SVG attributs as keyword-arguments
