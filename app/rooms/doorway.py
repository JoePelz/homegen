from app.rooms.base_wall import BaseWall


class Doorway(BaseWall):
    MIN_WIDTH = 43
    MAX_WIDTH = 43

    def __init__(self):
        super().__init__()
        self.template = 'doorway'  # type: str
