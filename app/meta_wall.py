class MetaWall:
    def __init__(self, template, name=None, is_door=False):
        self.template = template
        self.name = name
        self.is_door = is_door

        if name is None:
            self.name = "Doorway" if is_door else "Wall"


    def  __str__(self):
        desc = '<MetaWall({type}, {template}) "{name}">'.format(
            type="Doorway" if self.is_door else "Wall",
            template=self.template,
            name=self.name
        )
        return desc

    def __repr__(self):
        defn = "MetaWall(template='{template}', name='{name}', is_door={door})".format(
            template=self.template,
            name=self.name,
            door=self.is_door
        )
        return defn

    def dup(self):
        copy = MetaWall(
            template = self.template,
            name = self.name,
            is_door = self.is_door
        )
        return copy