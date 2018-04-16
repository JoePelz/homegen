import operator
import random
from typing import List, Tuple
from app.rooms import *
from app.graph import Graph
from app.requirements import Requirements
from app.meta_room import MetaRoom
from app.meta_wall import MetaWall
from app.edge import Edge
from app.transform import Transform2D


class NoAttachmentPointError(Exception):
    def __init__(self, node: Graph):
        self.node = node


class InvalidGraphError(Exception):
    pass


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

        # Turn all the metarooms into real rooms with sizes, and walls between them.
        try:
            Modeler.make_rooms(graph.children[0])
        except NoAttachmentPointError as e:
            raise InvalidGraphError('Too many branches from one graph node. (Attempted to connect {} rooms'
                                    ' to room: "{}")'.format(len(e.node.children) + 1, e.node.contents.name))

        all_models = Modeler.list_of_rooms(graph)
        return all_models

    @staticmethod
    def initialize_room(room: BaseRoom, width: float, depth: float) -> None:
        room.set_box(width, depth)
        room.set_square_inches(width * depth)
        room.set_ratio(width / depth)

    @staticmethod
    def make_rooms(graph: Graph) -> None:
        attachment_edges = graph.parent.model.get_attachment_points()  # type: List[Edge]
        if not attachment_edges:
            raise NoAttachmentPointError(graph)
        attachment_edge = random.choice(attachment_edges)  # type: Edge
        attachment_edge.mark_used()
        room = Modeler.instantiate(graph.contents)
        width = random.randint(room.MIN_WIDTH, room.MAX_WIDTH)
        depth = random.randint(room.MIN_DEPTH, room.MAX_DEPTH)
        Modeler.initialize_room(room, width, depth)

        print("Attaching {} to {}".format(room.name, graph.parent.model.name))
        room.transform = Modeler.calc_xform(graph.parent.model.transform, attachment_edge).normalize()

        graph.model = room
        for child in graph.children:
            Modeler.make_rooms(child)

    @staticmethod
    def calc_xform(parent_xform: Transform2D, edge: Edge) -> Transform2D:
        rel_x = tuple(map(operator.sub, edge.start, edge.end))
        rel_y = (-rel_x[1], rel_x[0])
        rel_p = edge.center
        rel_xform = Transform2D((*rel_x, *rel_y, *rel_p))

        xform = (parent_xform * rel_xform).normalize()
        # print("parent: {}".format(parent_xform))
        # print("local:  {}".format(rel_xform))
        # print("result: {}\n".format(xform))
        return xform

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
