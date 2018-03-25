import random
from app.Rooms import BaseRoom


class Hallway (BaseRoom):
    MIN_SIZE = 43

    def __init__(self):
        long_side = random.randrange(Hallway.MIN_SIZE, 360)
        if random.getrandbits(1) == 1:
            super(long_side, Hallway.MIN_SIZE)
        else:
            super(Hallway.MIN_SIZE, long_side)
