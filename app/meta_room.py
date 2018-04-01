class MetaRoom:
    def __init__(self, template, name, min_count=1, max_count=1):
        self.template = template
        self.name = name
        self.min_count = min_count
        self.max_count = max_count

    def  __str__(self):
        desc = '<MetaRoom({template}) "{name}" x{min}..{max}>'.format(
            template=self.template,
            name=self.name,
            min=self.min_count,
            max=self.max_count
        )
        return desc

    def __repr__(self):
        defn = "MetaRoom(template='{template}', name='{name}', min_count={min}, max_count={max})".format(
            template=self.template,
            name=self.name,
            min=self.min_count,
            max=self.max_count
        )
        return defn

    def dup(self):
        copy = MetaRoom(
            self.template,
            self.name,
            self.min_count,
            self.max_count
        )
        return copy