from app.meta_room import MetaRoom


class MetaWall(MetaRoom):
    def __init__(self, template: str, name: str=None, is_door: bool=True):
        super().__init__(template, name, min_count=1, max_count=1)
        self.is_door = is_door  # type: bool

        if name is None:
            self.name = "Doorway" if is_door else "Wall"

    def  __str__(self) -> str:
        desc = '<MetaWall({type}, {template}) "{name}">'.format(
            type="Doorway" if self.is_door else "Wall",
            template=self.template,
            name=self.name
        )
        return desc

    def __repr__(self) -> str:
        defn = "MetaWall(template='{template}', name='{name}', is_door={door})".format(
            template=self.template,
            name=self.name,
            door=self.is_door
        )
        return defn

    def dup(self) -> 'MetaWall':
        copy = MetaWall(
            template = self.template,
            name = self.name,
            is_door = self.is_door
        )
        return copy