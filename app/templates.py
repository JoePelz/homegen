import os
import yaml
import app


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

    @classmethod
    def load_templates(cls):
        raw_data = cls.load_file(os.path.join(APP_ROOT, 'templates', 'default_rooms.yml'))

        print("yaml:")
        print(raw_data)
        print(raw_data['base_room'])
        print(raw_data['base_room']['constraints'])

        templates = {}
        for k, v in raw_data.items():
            templates[k] = v
            templates[k]['constraints'] = cls.gather_constraints(v, raw_data)

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
