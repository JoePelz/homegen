class MetaRoom:
    def __init__(self, template, name, min_count=1, max_count=1):
        self.template = template
        self.name = name
        self.min_count = min_count
        self.max_count = max_count
