import random
from app.meta_room import MetaRoom
from app.grapher import Grapher


class Architect:
    def __init__(self):
        self.requirements = {}
        self.graph = None
        self.models = []
        self.blueprints = None

    def load_requirements(self, yaml):
        print("\n=== Loading ===\n")

        rooms = []
        constraints = []
        y_rooms = yaml['home']['rooms']
        for room in y_rooms:
            template = room.get('template', 'BaseRoom')
            name = room.get('name', 'Room')
            min_count = room.get('min_count', 1)
            max_count = room.get('max_count', 1)
            mr = MetaRoom(template, name, min_count, max_count)
            rooms.append(mr)

        self.requirements = {
            'rooms': rooms,
            'constraints': constraints
        }
        return self.requirements

    def graph_from_requirements(self):
        print("\n=== Graphing ===\n")
        self.graph = Grapher.build_graph(self.requirements['rooms'])

        print("\n=== Done ===\n")
        Grapher.draw_tree(self.graph)

    def models_from_graph(self):
        pass

    def blueprints_from_models(self):
        pass
