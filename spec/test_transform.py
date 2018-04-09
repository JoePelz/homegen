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


def test_multiply():
    i = Transform2D.identity()
    a = Transform2D((1, 2, 3, 4, 5, 6))
    b = Transform2D((9, 8, 7, 6, 5, 4))
    c = Transform2D((33, 50, 25, 38, 22, 32))
    assert i * a == a
    assert a * i == a
    assert a * b == c


