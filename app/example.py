import os
from app.architect import Architect
import yaml


def test_run():
    with open("../example/home.yaml") as f:
        raw_data = f.read()
    data = yaml.load(raw_data)

    arch = Architect()
    arch.load_requirements(data)
    arch.graph_from_requirements()
    arch.models_from_graph()
    arch.blueprints_from_models()


if __name__ == '__main__':
    test_run()
