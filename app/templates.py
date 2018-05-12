from typing import Dict
import os
import yaml
import app

from app import constraints


APP_ROOT = os.path.join(os.path.dirname(app.__file__))


class Templates:
    templates = None

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
    def import_constraint(raw: Dict) -> constraints.BaseConstraint:
        if isinstance(raw, constraints.BaseConstraint):
            return raw

        type = raw['type']
        instance = None
        if type in constraints.mapping:
            instance = constraints.mapping[type](**raw.get('attributes', {}))
        return instance

    @classmethod
    def load_templates(cls):
        raw_data = cls.load_file(os.path.join(APP_ROOT, 'templates', 'default_rooms.yml'))

        templates = {}
        for name, properties in raw_data.items():
            templates[name] = properties
            templates[name]['constraints'] = [c for c in map(cls.import_constraint, cls.gather_constraints(properties, raw_data)) if c]

        cls.templates = templates

    @classmethod
    def gather_constraints(cls, template, templates):
        if 'parent' in template and template['parent'] in templates:
            return cls.gather_constraints(templates[template['parent']], templates) + template['constraints']
        return template['constraints']

    @classmethod
    def get_template_constraints(cls, template_name):
        if not cls.templates:
            cls.load_templates()

        if template_name not in cls.templates:
            return []
        return cls.templates[template_name]['constraints']
