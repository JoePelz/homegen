from app.modeler import Modeler
from app.graph import Graph
from app.meta_room import MetaRoom
from app.meta_wall import MetaWall
from app.rooms import Hallway, Doorway, Entrance, Flex
from app.transform import Transform2D
import random

def test_make_rooms(monkeypatch):
    metaroom3 = MetaRoom('hallway', 'Side Hallway')
    metaroom4 = MetaWall('doorway', 'Kitchen Door')

    room3 = Hallway(); room3.name='Side Hallway'; room3.set_box(43, 263); room3.transform = Transform2D((1, 0, 0, 1, 0, 48))

    graph3 = Graph(contents=metaroom3, model=room3)
    graph4 = Graph(contents=metaroom4, parent=graph3)
    graph3.children.append(graph4)

    def mock_attachment():
        return [graph3.model.edges[0]]
    monkeypatch.setattr(graph3.model, 'get_attachment_points', mock_attachment)
    Modeler.make_rooms(graph4)
    assert graph4.model.transform == (-1, 0, 0, -1, 0, 48)

    def mock_attachment():
        return [graph3.model.edges[1]]
    monkeypatch.setattr(graph3.model, 'get_attachment_points', mock_attachment)
    Modeler.make_rooms(graph4)
    assert graph4.model.transform == (0, -1, 1, 0, 21.5, 179.5)

    def mock_attachment():
        return [graph3.model.edges[2]]
    monkeypatch.setattr(graph3.model, 'get_attachment_points', mock_attachment)
    Modeler.make_rooms(graph4)
    assert graph4.model.transform == (1, 0, 0, 1, 0, 311)

    def mock_attachment():
        return [graph3.model.edges[3]]
    monkeypatch.setattr(graph3.model, 'get_attachment_points', mock_attachment)
    Modeler.make_rooms(graph4)
    assert graph4.model.transform == (0, 1, -1, 0, -21.5, 179.5)

