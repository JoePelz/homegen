import yaml
from app.meta_room import MetaRoom
from app.requirements import Requirements


class InvalidRequirements (Exception):
    pass


class RequirementsImporter:
    @staticmethod
    def load_file(path: str) -> dict:
        """
        Open the given yaml file and parse it into a dictionary structure.

        :param path: The file path to open.
        :return: The parsed dictionary.
        """
        with open(path) as f:
            raw_data = f.read()
        data = yaml.load(raw_data)
        return data

    @staticmethod
    def validate(root: dict) -> bool:
        """
        Check if the yaml dict is a valid requirements file.
        :param root: The yaml dict object
        :return: True if valid
        """
        return True

    @staticmethod
    def parse(root: dict) -> Requirements:
        """
        Take a yaml dict and parse it into meta_rooms and meta_constraints.
        :param root: The yaml dict object
        :return: A requirements object.
        """
        requirements = Requirements()

        yaml_rooms = root['home']['rooms']
        for room in yaml_rooms:
            template = room.get('template', 'BaseRoom').lower()
            name = room.get('name', 'Room')
            min_count = int(room.get('min_count', 1))
            max_count = int(room.get('max_count', 1))
            constraints = room.get('constraints')
            # TODO: constraints here should reflect defaults constraints from the template
            #   as well as constraints from the yaml file.
            mr = MetaRoom(template, name, min_count, max_count, constraints)
            requirements.add_room(mr)

        return requirements

    @staticmethod
    def load(path: str) -> Requirements:
        """
        Load, validate and parse the requirements.yaml file into a
        requirements object.

        :param path: The path for the requirements.yaml file
        :return: The imported requirements
        """
        root = RequirementsImporter.load_file(path)
        if not RequirementsImporter.validate(root):
            raise InvalidRequirements
        requirements = RequirementsImporter.parse(root)
        return requirements
