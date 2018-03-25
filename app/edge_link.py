# Edge links determine which edges are meant to be parallel and overlapping (coincident)
# Their start and end points may not match exactly, as lines AD and BC show:
#        *---*--------------*-----*
#        A   B              C     D


class EdgeLink:
    def __init__(self):
        # `self.aligned` is a list of edges that should be aligned.
        # full relation is:
        # Room - 1..* - Edge
        # Wall - 1..* - Edge
        # Edge - 2..1 - EdgeLink
        # so rooms and walls have many edges, and some edges are connected via edge-links.
        self.aligned = []
