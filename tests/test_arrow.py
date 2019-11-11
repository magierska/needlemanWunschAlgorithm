import pytest
from arrow import Arrow


def test_init():
    x_start = 0
    y_start = 1
    x_end = 2
    y_end = 3
    arrow = Arrow(x_start, y_start, x_end, y_end)
    assert arrow.start.x == x_start
    assert arrow.start.y == y_start
    assert arrow.end.x == x_end
    assert arrow.end.y == y_end


def test_create_seq():
    arrow = Arrow(0, 0, 0, 0)
    with pytest.raises(NotImplementedError):
        arrow.create_seq('', '')
