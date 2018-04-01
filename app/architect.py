from app.meta_room import MetaRoom
from app.grapher import Graph
from app.requirements import Requirements
from app.requirements_importer import RequirementsImporter


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

        Graph.draw_tree(graph)
        return graph

    @staticmethod
    def models_from_graph(requirements: Requirements, root: Graph) -> list:
        """

        :param requirements: Requirements object with the constraints to use
        :param root: Graph of nodes with rooms/doorways
        :return: List of rooms and walls with finalized size/shape/position
        """
        print("\n=== Modeling ===\n")
        # Tasks:
        # - Create a list of room objects from the meta_room objects
        # - Create a list of constraints that bind the room objects
        # - Iteratively solve the constraints??
        # - Wrap entire house with exterior walls
        # Output:
        # - List of rooms and walls with finalized size/shape/position
        print("\n=== Done ===\n")

        return []

    @staticmethod
    def blueprints_from_models(rooms: list) -> str:
        """


        :param rooms:
        :return: path to svg file to view
        """
        return "/"
