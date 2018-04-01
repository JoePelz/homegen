from app.meta_room import MetaRoom
from app.meta_wall import MetaWall
import random


class Node:
    def __init__(self):
        self.parent = None
        self.children = []
        self.contents = None

    def __str__(self):
        return self.contents.name if self.contents else "empty"


class Grapher:
    @staticmethod
    def list_all_rooms(requirements):
        all_rooms = []
        for req in requirements:
            for i in range(1, random.randint(req.min_count, req.max_count) + 1):
                all_rooms.append(req.dup())
        return all_rooms

    @staticmethod
    def pick_node_to_grow(nodelist):
        size = len(nodelist)
        choice = None
        while choice == None:
            suggestion = nodelist[random.randint(0, size - 1)]
            # do not pick walls that already open into rooms
            if isinstance(suggestion.contents, MetaWall) and len(suggestion.children) > 0:
                continue
            choice = suggestion
        return choice

    @staticmethod
    def attach_room_to_node(room, node, nodelist):
        wall_node = Node()
        wall_node.contents = MetaWall("base_wall", "{} Door".format(room.name), is_door=True)
        room_node = Node()
        room_node.contents = room

        room_node.parent = wall_node
        wall_node.children.append(room_node)
        wall_node.parent = node
        node.children.append(wall_node)

        nodelist.append(wall_node)
        nodelist.append(room_node)

    @staticmethod
    def draw_tree(root, indent=0):
        print("{prefix}{node}".format(
            prefix=indent*"-",
            node=root,
            parent=root.parent
        ))
        for child in root.children:
            Grapher.draw_tree(child, indent+1)

    @staticmethod
    def make_root():
        entrance = MetaWall("base_wall", "Entrance", True)
        root = Node()
        root.contents = entrance
        return root

    @staticmethod
    def build_graph(requirements):
        rooms = Grapher.list_all_rooms(requirements)
        random.shuffle(rooms)
        root = Grapher.make_root()
        nodes = [root]

        for room in rooms:
            attachment_point = Grapher.pick_node_to_grow(nodes)
            Grapher.attach_room_to_node(room, attachment_point, nodes)

        return root