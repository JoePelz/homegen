class MetaRoom:
    def __init__(self, template: str, name: str, min_count: int=1, max_count: int=1):
        self.template = template  # type: str
        self.name = name  # type: str
        self.min_count = min_count  # type: int
        self.max_count = max_count  # type: int

    def  __str__(self) -> str:
        desc = '<MetaRoom({template}) "{name}" x{min}..{max}>'.format(
            template=self.template,
            name=self.name,
            min=self.min_count,
            max=self.max_count
        )
        return desc

    def __repr__(self) -> str:
        defn = "MetaRoom(template='{template}', name='{name}', min_count={min}, max_count={max})".format(
            template=self.template,
            name=self.name,
            min=self.min_count,
            max=self.max_count
        )
        return defn

    def dup(self) -> 'MetaRoom':
        copy = MetaRoom(
            self.template,
            self.name,
            self.min_count,
            self.max_count
        )
        return copy
