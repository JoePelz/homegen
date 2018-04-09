from typing import List
from app.graph import Graph
from app.requirements import Requirements
from app.requirements_importer import RequirementsImporter
from app.modeler import Modeler
from app.rooms import BaseRoom
from app.blueprint import Blueprint


class Architect:
    @staticmethod
    def load_requirements(path: str) -> Requirements:
        """
        Load a yaml file and parse it into requirements for rooms
        and constraints.

        :param path: The path to a yaml file describing
        the room requirements and extra constraints.
        :return: A Requirements object listing the rooms and constraints
        determined from the input yaml.
        """
        print("\n=== Loading ===\n")

        requirements = RequirementsImporter.load(path)
        requirements.room_report()

        return requirements

    @staticmethod
    def graph_from_requirements(requirements: Requirements) -> Graph:
        """
        Take the requirements and make a graph of the connectivity of rooms
        in the house.

        :param requirements: The Requirements object listing all the rooms to
        include in the house
        :return: A tree of all the paths through the house start at the
        main entrance.
        """

        print("\n=== Graphing ===\n")
        graph = Graph.build_graph(requirements)

        # graph.children[0].children[0].children = []

        Graph.draw_tree(graph, draw_doors=False)
        return graph

    @staticmethod
    def models_from_graph(requirements: Requirements, root: Graph) -> List[BaseRoom]:
        """
        :param requirements: Requirements object with the constraints to use
        :param root: Graph of nodes with rooms/doorways
        :return: List of rooms and walls with finalized size/shape/position
        """
        print("\n=== Modeling ===\n")
        models = Modeler.convert_graph(requirements, root)
        # for model in models:
        #     print(model.report())
        return models

    @staticmethod
    def blueprints_from_models(models: List[BaseRoom], name: str="blueprints.svg") -> str:
        """
        :param name:
        :param models:
        :return: path to svg file to view
        """
        print("\n=== Blueprinting ===\n")
        blueprint = Blueprint(path=name)
        for model in models:
            blueprint.add_model(model)
        blueprint.export()

        print("\n=== Done ===\n")
        return "/"
