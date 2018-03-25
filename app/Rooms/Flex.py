import random
from app.Rooms import BaseRoom


class Flex(BaseRoom):
    MIN_SIZE = 72

    def __init__(self):
        x_size = random.randrange(Flex.MIN_SIZE, 150)
        y_size = random.randrange(Flex.MIN_SIZE, 150)
        super(x_size, y_size)
