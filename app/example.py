import os
import app
from app.architect import Architect
from app.requirements import Requirements
from app.meta_room import MetaRoom
from app.meta_wall import MetaWall
from app.graph import Graph
from app import rooms
from app.transform import Transform2D
from app.blueprint import Blueprint

APP_ROOT = os.path.join(os.path.dirname(app.__file__), os.path.pardir)


def get_sample_requirements():
    reqs = Requirements()
    reqs.rooms = [
        MetaRoom(template='hallway', name='Main Hallway', min_count=1, max_count=1),
        MetaRoom(template='hallway', name='Side Hallway', min_count=1, max_count=1),
        MetaRoom(template='closet', name='Closet1', min_count=1, max_count=1),
        MetaRoom(template='closet', name='Closet2', min_count=1, max_count=1),
        MetaRoom(template='flex', name='Bathroom', min_count=1, max_count=1),
        MetaRoom(template='flex', name='Kitchen', min_count=1, max_count=1),
        MetaRoom(template='flex', name='Flex', min_count=1, max_count=1),
        MetaRoom(template='flex', name='Bedroom', min_count=1, max_count=1),
        MetaRoom(template='flex', name='Patio', min_count=1, max_count=1)
    ]
    return reqs


def get_sample_graph():
    # graph:
    #   parent:
    #   contents: MetaRoom/MetaWall
    #   model: None (for now. Becomes rooms.BaseRoom later)
    #   children: List[Graph]
    root = Graph(contents=MetaWall(template='entrance', name='Entrance'))

    front_door = Graph(parent=root, contents=MetaWall(template='doorway', name='Main Hallway Door'))
    root.children.append(front_door)

    hallway = Graph(parent=front_door, contents=MetaRoom(template='hallway', name='Main Hallway'))
    front_door.children.append(hallway)

    closet_door = Graph(parent=hallway, contents=MetaWall(template='doorway', name='Closet Door'))
    hallway.children.append(closet_door)

    closet = Graph(parent=closet_door, contents=MetaRoom(template='closet', name='Closet'))
    closet_door.children.append(closet)

    bathroom_door = Graph(parent=hallway, contents=MetaWall(template='doorway', name='Bathroom Door'))
    hallway.children.append(bathroom_door)

    bathroom = Graph(parent=bathroom_door, contents=MetaRoom(template='flex', name='Bathroom'))
    bathroom_door.children.append(bathroom)

    return root


def get_sample_models():
    # room:
    #    edges = []  # type: List[Edge]
    #    base_edge = 0  # type: int
    #    square_inches = 0.  # type: float
    #    ratio = 0.  # type: float
    #    name = ""  # type: str
    #    id = ""  # type: str
    #    template = 'base'  # type: str
    #    transform = Transform2D.identity()  # type: Transform2D
    entrance = rooms.Entrance()
    entrance.set_box(43, 43); entrance.set_square_inches(1849); entrance.set_ratio(1.0)
    entrance.name = 'Entrance'; entrance.id = 'entrance'

    hallway_door = rooms.Doorway()
    hallway_door.set_box(43, 5); hallway_door.set_square_inches(215); hallway_door.set_ratio(8.6)
    hallway_door.name = 'Main Hallway Door'; hallway_door.id = 'main_hallway_door'
    hallway_door.transform = Transform2D((1, 0, 0, 1, 0, 43))

    hallway = rooms.Hallway()
    hallway.set_box(43, 133); hallway.set_square_inches(5719); hallway.set_ratio(0.3233)
    hallway.name = 'Main Hallway'; hallway.id = 'main_hallway'
    hallway.transform = Transform2D((1, 0, 0, 1, 0, 48))

    closet_door = rooms.Doorway()
    closet_door.set_box(43, 5); closet_door.set_square_inches(215); closet_door.set_ratio(8.6)
    closet_door.name = 'Closet Door'; closet_door.id = 'closet_door'
    closet_door.transform = Transform2D((0, -1, 1, 0, 21.5, 114.5))

    closet = rooms.Closet()
    closet.set_box(47, 25); closet.set_square_inches(1175); closet.set_ratio(1.88)
    closet.name = 'Closet'; closet.id = 'closet'
    closet.transform = Transform2D((0, -1, 1, 0, 26.5, 114.5))

    bathroom_door = rooms.Doorway()
    bathroom_door.set_box(47, 5); bathroom_door.set_square_inches(1175); bathroom_door.set_ratio(8.6)
    bathroom_door.name = 'Bathroom Door'; bathroom_door.id = 'bathroom_door'
    bathroom_door.transform = Transform2D((1, 0, 0, 1, 0, 181))

    bathroom = rooms.Flex()
    bathroom.set_box(137, 98); bathroom.set_square_inches(13426); bathroom.set_ratio(1.398)
    bathroom.name = 'Bathroom'; bathroom.id = 'bathroom'
    bathroom.transform = Transform2D((1, 0, 0, 1, 0, 186))

    models = [entrance, hallway_door, hallway, closet_door, closet, bathroom_door, bathroom]
    return models


def get_sample_dwg():
    models = get_sample_models()
    blueprint = Blueprint()
    for model in models:
        blueprint.add_model(model)
    blueprint.resize_viewbox(30)
    return blueprint.dwg


def test_run():
    example_path = os.path.join(APP_ROOT, 'example', 'home.yaml')

    arch = Architect()
    requirements = arch.load_requirements(example_path)
    graph = arch.graph_from_requirements(requirements)
    models = arch.models_from_graph(requirements, graph)
    outpath = arch.blueprints_from_models(models)
    print("Out: {}".format(outpath))


if __name__ == '__main__':
    test_run()
