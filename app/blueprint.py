from typing import List
from app.rooms import BaseRoom
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
        if model.is_a_wall():
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
        points = self.__class__.recursive_point_collector(tree)
        min_x = 0
        max_x = 0
        min_y = 0
        max_y = 0
        for x, y in points:
            if x < min_x:
                min_x = x
            elif x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            elif y > max_y:
                max_y = y

        self.dwg.viewbox(
            min_x - margin,
            min_y - margin,
            (max_x - min_x) + 2 * margin,
            (max_y - min_y) + 2 * margin)

    @classmethod
    def recursive_point_collector(cls, node):
        # points from children
        # add points from local
        # multiply by local transform
        # return all points.
        child_points = []
        for child in node.getchildren():
            if child.tag in ['g', 'polygon']:
                child_points.extend(cls.recursive_point_collector(child))
        if node.get('points'):
            local_points = [tuple(map(float, p.split(','))) for p in node.get('points').split(' ')]
        else:
            local_points = []

        points = child_points + local_points

        if node.get('transform'):
            local_transform = Transform2D(tuple(map(float, node.get('transform').strip("matrix()").split(","))))
        else:
            local_transform = Transform2D.identity()

        points = [local_transform.multiply_point(p) for p in points]
        return points

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

    def render_wall(self, model) -> svgwrite.container.Group:
        points = map(lambda m: m.start, model.edges)
        matrix = self.__class__.transform_to_svg(model.transform)
        polygon = self.dwg.polygon(
            points,
            class_='wall',
        )
        return self.group(polygon, room_id=model.id, matrix=model.transform)

    @staticmethod
    def transform_to_svg(transform: Transform2D) -> List[float]:
        # This was made when I had Transform2D in another order,
        # but is now basically a noop getting the values.
        index_order = 0, 1, 2, 3, 4, 5
        matrix = [transform.values[i] for i in index_order]
        return matrix

# Polyline.__init__(points=[], **extra)
# Parameters:
# points (iterable) – iterable of points (points are 2-tuples)
# extra – additional SVG attributs as keyword-arguments
