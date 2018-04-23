from typing import Tuple


class Transform2D:
    def __init__(self, values: Tuple[float, float, float, float, float, float]):
        self.values = values  # type: Tuple[float, float, float, float, float, float]

    def normalize(self) -> 'Transform2D':
        x_len = (self.values[0]**2 + self.values[1]**2)**0.5
        y_len = (self.values[2]**2 + self.values[3]**2)**0.5
        xx = self.values[0] / x_len
        xy = self.values[1] / x_len
        yx = self.values[2] / y_len
        yy = self.values[3] / y_len
        out = (xx, xy, yx, yy, self.values[4], self.values[5])
        return Transform2D(out)

    def multiply_point(self, other: Tuple[float, float]):
        a, b = other
        xx, xy, yx, yy, px, py = self.values
        x = a*xx + b*yx + px
        y = a*xy + b*yy + py
        return x, y

    def __mul__(self, other: 'Transform2D') -> 'Transform2D':
        if isinstance(other, Transform2D):
            a = self.values
            b = other.values
            # arow1 = a0, a2, a4
            # arow2 = a1, a3, a5
            # bcol1 = b0, b1, 0
            # bcol2 = b2, b3, 0
            # bcol3 = b4, b5, 1
            # c0 = arow1, bcol1
            c0 = a[0]*b[0] + a[2]*b[1]
            # c1 = arow2, bcol1
            c1 = a[1]*b[0] + a[3]*b[1]
            # c2 = arow1, bcol2
            c2 = a[0]*b[2] + a[2]*b[3]
            # c3 = arow2, bcol2
            c3 = a[1]*b[2] + a[3]*b[3]
            # c4 = arow1, bcol3
            c4 = a[0]*b[4] + a[2]*b[5] + a[4]
            # c5 = arow2, bcol3
            c5 = a[1]*b[4] + a[3]*b[5] + a[5]
            return Transform2D((c0, c1, c2, c3, c4, c5))
        else:
            raise ArithmeticError

    def __eq__(self, other) -> bool:
        if isinstance(other, Transform2D):
            return self.values == other.values
        elif isinstance(other, tuple):
            return self.values == other
        else:
            return False

    @staticmethod
    def identity() -> 'Transform2D':
        return Transform2D((1, 0, 0, 1, 0, 0))

    def get_pos(self) -> Tuple[float, float]:
        return self.values[4], self.values[5]

    def __str__(self) -> str:
        return str(self.values)

    def __repr__(self) -> str:
        return repr(self.values)