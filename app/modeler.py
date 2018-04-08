import operator
import random
from typing import List, Tuple
from app.rooms import *
from app.graph import Graph
from app.requirements import Requirements
from app.meta_room import MetaRoom
from app.meta_wall import MetaWall
from app.edge import Edge


class Modeler:
    @staticmethod
    def convert_graph(requirements: Requirements, graph: Graph) -> List[BaseRoom]:
        """
        Convert Requirements and a graph of rooms into a set of room models
        with sizes and positions.

        :param requirements: The Requirements object with constraints to
        observe.
        :param graph: Graph object defining the connectivity of rooms.
        :return: List of rooms and walls with finalized size/shape/position
        """

        # Tasks:
        # - Create a list of room objects from the meta_room objects
        # - Define all the constraints that bind the room objects
        # - Iteratively solve the constraints??
        # - Wrap entire house with exterior walls

        # entrance ("porch"? Not really part of the house)
        graph.model = Modeler.instantiate(graph.contents)
        Modeler.initialize_room(graph.model, width=43, depth=43)
        print("modeling {}".format(graph.model.report()))
        Modeler.make_rooms(graph.children[0])

        all_models = Modeler.list_of_rooms(graph)
        return all_models

    @staticmethod
    def initialize_room(room: BaseRoom, width: float, depth: float) -> None:
        room.set_box(width, depth)
        room.set_square_inches(width * depth)
        room.set_ratio(width / depth)

    @staticmethod
    def make_rooms(graph: Graph) -> None:
        attachment_edge = random.choice(graph.parent.model.get_attachment_points())  # type: Edge
        room = Modeler.instantiate(graph.contents)
        width = random.randint(room.MIN_WIDTH, room.MAX_WIDTH)
        depth = random.randint(room.MIN_DEPTH, room.MAX_DEPTH)
        Modeler.initialize_room(room, width, depth)

        x_axis = tuple(map(operator.sub, attachment_edge.start, attachment_edge.end))

        xform = graph.parent.model.transform
        px, py = xform[2], xform[5]
        rel_x, rel_y = attachment_edge.center
        cx = rel_x * xform[0] + rel_y * xform[3]
        cy = rel_x * xform[1] + rel_y * xform[4]
        center = cx+px, cy+py
        # room.set_transform(x_axis, center)

        # TODO: test after calc_xform works
        room.transform = Modeler.calc_xform(graph.parent.model.transform, attachment_edge)

        graph.model = room
        for child in graph.children:
            Modeler.make_rooms(child)

    @staticmethod
    def calc_xform(parent_xform: Tuple[float, float, float, float, float, float], edge: Edge):
        rel_x = tuple(map(operator.sub, edge.start, edge.end))
        rel_y = (-rel_x[1], rel_x[0])
        rel_p = edge.center
        rel_xform = (*rel_x, *rel_y, *rel_p)
        assert len(rel_xform) == len(parent_xform)

        # TODO: return rel_xform * parent_xform
        return "???"

    @staticmethod
    def instantiate(metaroom: MetaRoom) -> BaseRoom:
        if metaroom.template == 'closet':
            room = Closet()
        elif metaroom.template == 'flex':
            room = Flex()
        elif metaroom.template == 'hallway':
            room = Hallway()
        elif metaroom.template == 'doorway':
            room = Doorway()
        elif metaroom.template == 'wall':
            room = BaseWall()
        elif metaroom.template == 'entrance':
            room = Entrance()
        else:
            room = BaseRoom()
        room.name = metaroom.name
        return room

    @staticmethod
    def list_of_rooms(graph: Graph) -> List[BaseRoom]:
        rooms = []
        if graph.model:
            rooms.append(graph.model)
        for child in graph.children:
            rooms.extend(Modeler.list_of_rooms(child))
        return rooms
