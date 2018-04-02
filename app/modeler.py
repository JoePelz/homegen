import operator
import random
from typing import List
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
        graph.model = BaseRoom()
        graph.model.set_box(43, 43)

        # entrance door
        # door = graph.children[0]
        # door.model = Doorway()
        # door.model.set_box(43, Doorway.MIN_DEPTH)
        Modeler.make_rooms(graph.children[0])

        all_models = Modeler.list_of_rooms(graph)
        return all_models

    @staticmethod
    def make_rooms(graph: Graph):
        attachment_edge = random.choice(graph.parent.model.get_attachment_points())  # type: Edge
        room = Modeler.instantiate(graph.contents)
        width = random.randint(room.MIN_WIDTH, room.MAX_WIDTH)
        depth = random.randint(room.MIN_DEPTH, room.MAX_DEPTH)
        room.set_box(width, depth)

        x_axis = tuple(map(operator.sub, attachment_edge.end, attachment_edge.start))

        xform = graph.parent.model.transform
        px, py = xform[2], xform[5]
        rel_x, rel_y = attachment_edge.center
        cx = rel_x * xform[0] + rel_y * xform[1]
        cy = rel_x * xform[3] + rel_y * xform[4]
        center = cx+px, cy+py

        room.set_transform(x_axis, center)

        graph.model = room
        for child in graph.children:
            Modeler.make_rooms(child)

    @staticmethod
    def instantiate(room: MetaRoom):
        if room.template == 'closet':
            return Closet()
        elif room.template == 'flex':
            return Flex()
        elif room.template == 'hallway':
            return Hallway()
        elif room.template == 'doorway':
            return Doorway()
        elif room.template == 'wall':
            return BaseWall()
        else:
            return BaseRoom()

    @staticmethod
    def list_of_rooms(graph: Graph) -> List[BaseRoom]:
        rooms = []
        if graph.model:
            rooms.append(graph.model)
        for child in graph.children:
            rooms.extend(Modeler.list_of_rooms(child))
        return rooms
