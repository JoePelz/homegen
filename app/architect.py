from typing import List
from app.graph import Graph
from app.requirements import Requirements
from app.requirements_importer import RequirementsImporter
from app.modeler import Modeler
from app.rooms import BaseRoom


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
        for model in models:
            print(model.report())
        return models

    @staticmethod
    def blueprints_from_models(rooms: list) -> str:
        """


        :param rooms:
        :return: path to svg file to view
        """
        print("\n=== Done ===\n")
        return "/"
