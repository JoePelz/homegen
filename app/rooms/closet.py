from app.rooms.base_room import BaseRoom


class Closet(BaseRoom):
    MIN_WIDTH = 36
    MIN_DEPTH = 24

    MAX_WIDTH = 60
    MAX_DEPTH = 36