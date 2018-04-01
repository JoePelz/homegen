from app.requirements import Requirements
from app.meta_wall import MetaWall
import random


class Graph:
    def __init__(self):
        self.parent = None
        self.children = []
        self.contents = None
        self.model = None

    def __str__(self) -> str:
        if self.model:
            return str(self.model)
        elif self.contents:
            return self.contents.name
        else:
            return 'empty'

    @staticmethod
    def list_all_rooms(requirements: Requirements) -> list:
        all_rooms = []
        for req in requirements.rooms:
            for i in range(1, random.randint(req.min_count, req.max_count) + 1):
                all_rooms.append(req.dup())
        return all_rooms

    @staticmethod
    def pick_node_to_grow(nodelist: list) -> 'Graph':
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
    def attach_room_to_node(room, node: 'Graph', nodelist: list) -> None:
        wall_node = Graph()
        wall_node.contents = MetaWall("base_wall", "{} Door".format(room.name), is_door=True)
        room_node = Graph()
        room_node.contents = room

        room_node.parent = wall_node
        wall_node.children.append(room_node)
        wall_node.parent = node
        node.children.append(wall_node)

        nodelist.append(wall_node)
        nodelist.append(room_node)

    @staticmethod
    def draw_tree(root: 'Graph', indent: int=0) -> None:
        print("{prefix}{node}".format(
            prefix=indent*"-",
            node=root,
            parent=root.parent
        ))
        for child in root.children:
            Graph.draw_tree(child, indent+1)

    @staticmethod
    def make_root() -> 'Graph':
        entrance = MetaWall("base_wall", "Entrance", True)
        root = Graph()
        root.contents = entrance
        return root

    @staticmethod
    def build_graph(requirements: Requirements) -> 'Graph':
        rooms = Graph.list_all_rooms(requirements)
        random.shuffle(rooms)
        root = Graph.make_root()
        nodes = [root]

        for room in rooms:
            attachment_point = Graph.pick_node_to_grow(nodes)
            Graph.attach_room_to_node(room, attachment_point, nodes)

        return root
