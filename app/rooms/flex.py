from app.rooms.base_room import BaseRoom


class Flex(BaseRoom):
    MIN_WIDTH = 72
    MIN_DEPTH = 72

    MAX_WIDTH = 150
    MAX_DEPTH = 150

    def __init__(self):
        super().__init__()
        self.template = 'flex'  # type: str
