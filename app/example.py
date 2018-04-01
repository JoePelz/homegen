from app.architect import Architect


def test_run():
    example_path = "../example/home.yaml"

    arch = Architect()
    requirements = arch.load_requirements(example_path)
    graph = arch.graph_from_requirements(requirements)
    models = arch.models_from_graph(requirements, graph)
    outpath = arch.blueprints_from_models(models)
    print("Out: {}".format(outpath))


if __name__ == '__main__':
    test_run()
