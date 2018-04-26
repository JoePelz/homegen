from app.templates import Templates


def test_get_template_constraints():
    assert Templates.get_template_constraints('base_room') == [
        {'type': 'initial_size',
         'attributes': {
            'min_width': 24,
            'max_width': 300,
            'min_depth': 24,
            'max_depth': 300}}
    ]

def test_inherited_constraints():
    assert Templates.get_template_constraints('base_wall') == [
        {'type': 'initial_size',
         'attributes': {
            'min_width': 24,
            'max_width': 300,
            'min_depth': 24,
            'max_depth': 300
        }},
        {'type': 'initial_size',
         'attributes': {
            'min_depth': 5,
            'max_depth': 5,
            'min_width': 5
        }},
        {'type': 'straight_passage'}
    ]

    assert Templates.get_template_constraints('doorway') == [
        {'type': 'initial_size',
         'attributes': {
            'min_width': 24,
            'max_width': 300,
            'min_depth': 24,
            'max_depth': 300
        }},
        {'type': 'initial_size',
         'attributes': {
            'min_depth': 5,
            'max_depth': 5,
            'min_width': 5
        }},
        {'type': 'straight_passage'},
        {'type': 'initial_size',
         'attributes': {
            'min_width': 43,
            'max_width': 43
        }},
    ]
