from operator import itemgetter
from app.Constraints import BaseConstraint


class MinSize (BaseConstraint):
    pass

    # def valid
    #     max_y = max(vertices, key=itemgetter(1))[1]
    #     min_y = min(vertices, key=itemgetter(1))[1]
    #     return (max_y - min_y) > min_y_size && same-for-x