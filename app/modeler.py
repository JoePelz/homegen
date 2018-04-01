from app.rooms import *
from app.graph import Graph
from app.requirements import Requirements
from app.meta_room import MetaRoom
from app.meta_wall import MetaWall


class Modeler:
    @staticmethod
    def convert_graph(requirements: Requirements, graph: Graph) -> list:
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
        root.model = BaseRoom()



    @staticmethod
    def instantiate(room: MetaRoom or MetaWall):
        if room.template == 'closet':
            return Closet()
        elif room.template == 'flex':
            return Flex()
        elif room.template == 'hallway':
            return Hallway()
        elif room.template == 'doorway':
            return Doorway()
        elif room.template == 'wall':
            return Wall()
        else:
            return BaseRoom()
