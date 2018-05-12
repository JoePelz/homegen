from .base_constraint import BaseConstraint
from .dead_end import DeadEnd
from .initial_size import InitialSize
from .straight_passage import StraightPassage
from .wall import Wall


mapping = {
    'dead_end': DeadEnd,
    'straight_passage': StraightPassage,
    'initial_size': InitialSize,
    'wall': Wall
}
