import os
import app
from app.architect import Architect

APP_ROOT = os.path.join(os.path.dirname(app.__file__), os.path.pardir)


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
