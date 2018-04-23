from app import rooms


class BaseConstraint:
    def apply(self, room: rooms.BaseRoom):
        raise NotImplementedError()
