from typing import List, Union
import random
from app.requirements import Requirements
from app.meta_room import MetaRoom
from app.meta_wall import MetaWall
from app.rooms.base_room import BaseRoom


class Graph:
    def __init__(self, parent: 'Graph'=None, children: List['Graph']=None, contents: Union[MetaRoom, MetaWall]=None, model: BaseRoom=None):
        """
        set up some instance variables.
        """
        self.parent = parent  # type: Graph
        self.children = children or []  # type: List(Graph)
        self.contents = contents  # type: MetaRoom or MetaWall
        self.model = model  # type: BaseRoom

    def __str__(self) -> str:
        if self.model:
            return str(self.model)
        elif self.contents:
            return self.contents.name
        else:
            return 'empty'

    @staticmethod
    def list_all_rooms(requirements: Requirements) -> List[MetaRoom ]:
        """

        :param requirements:
        :return:
        """
        all_rooms = []
        for req in requirements.rooms:
            for i in range(1, random.randint(req.min_count, req.max_count) + 1):
                all_rooms.append(req.dup())
        return all_rooms

    @staticmethod
    def pick_node_to_grow(nodelist: List['Graph']) -> 'Graph':
        size = len(nodelist)
        choice = None
        while choice is None:
            suggestion = nodelist[random.randint(0, size - 1)]
            # do not pick walls that already open into rooms
            if isinstance(suggestion.contents, MetaWall) and len(suggestion.children) > 0:
                continue
            choice = suggestion
        return choice

    @staticmethod
    def attach_room_to_node(room, node: 'Graph', nodelist: List['Graph']) -> None:
        wall_node = Graph()
        wall_node.contents = MetaWall("doorway", "{} Door".format(room.name), is_door=True)
        room_node = Graph()
        room_node.contents = room

        room_node.parent = wall_node
        wall_node.children.append(room_node)
        wall_node.parent = node
        node.children.append(wall_node)

        nodelist.append(wall_node)
        nodelist.append(room_node)

    @staticmethod
    def draw_tree(root: 'Graph', indent: int=0, draw_doors: bool=False) -> None:
        if isinstance(root.contents, MetaWall) and draw_doors is False:
            for child in root.children:
                Graph.draw_tree(child, indent, draw_doors)
        else:
            print("{prefix}{node}".format(
                prefix=indent*"-",
                node=root,
                parent=root.parent
            ))
            for child in root.children:
                Graph.draw_tree(child, indent+1, draw_doors)

    @staticmethod
    def make_root() -> 'Graph':
        entrance = MetaRoom("entrance", "Entrance")
        root = Graph()
        root.contents = entrance
        return root

    @staticmethod
    def build_graph(requirements: Requirements) -> 'Graph':
        rooms = Graph.list_all_rooms(requirements)
        random.shuffle(rooms)
        root = Graph.make_root()
        nodes = []

        # this order and excluding root from nodes prevents additional
        # rooms from attaching to the Entrance.
        attachment_point = root
        for room in rooms:
            Graph.attach_room_to_node(room, attachment_point, nodes)
            attachment_point = Graph.pick_node_to_grow(nodes)

        return root
