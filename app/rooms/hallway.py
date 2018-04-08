from app.rooms.base_room import BaseRoom


class Hallway (BaseRoom):
    MIN_WIDTH = 43
    MIN_DEPTH = 43

    MAX_WIDTH = 43
    MAX_DEPTH = 360

    def __init__(self):
        super().__init__()
        self.template = 'hallway'  # type: str
