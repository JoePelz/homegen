from app.transform import Transform2D


def test_normalize_identity():
    i1 = Transform2D.identity()
    assert i1.normalize() == i1


def test_eq():
    a = Transform2D((1, 2, 3, 4, 5, 6))
    b = Transform2D((1, 2, 3, 4, 5, 6))
    assert a == b
    c = (1, 2, 3, 4, 5, 6)
    assert a == c
    assert b == c


def test_normalize():
    a = Transform2D((10, 0, 0, 5, 123, 456))
    assert a.normalize() == (1, 0, 0, 1, 123, 456)


def test___mul__():
    i = Transform2D.identity()
    a = Transform2D((1, 2, 3, 4, 5, 6))
    b = Transform2D((9, 8, 7, 6, 5, 4))
    c = Transform2D((33, 50, 25, 38, 22, 32))
    assert i * a == a
    assert a * i == a
    assert a * b == c


def test_multiple_point():
    p = (5, -2)
    movement = Transform2D((1, 0, 0, 1, 10, 100))
    assert movement.multiply_point(p) == (15, 98)
    rotation0 = Transform2D((1, 0, 0, 1, 0, 0))
    assert rotation0.multiply_point(p) == (5, -2)
    rotation1 = Transform2D((0, -1, 1, 0, 0, 0))
    assert rotation1.multiply_point(p) == (-2, -5)
    rotation2 = Transform2D((-1, 0, 0, -1, 0, 0))
    assert rotation2.multiply_point(p) == (-5, 2)
    rotation3 = Transform2D((0, 1, -1, 0, 0, 0))
    assert rotation3.multiply_point(p) == (2, 5)
    everything = Transform2D((1, 2, 3, 4, 5, 6))
    assert everything.multiply_point(p) == (4, 8)