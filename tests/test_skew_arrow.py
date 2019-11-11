from skewArrow import SkewArrow
from sequences import Sequences


def test_create_seq():
    x_start = 1
    y_start = 2
    arrow = SkewArrow(x_start, y_start, x_start - 1, y_start - 1)
    x_seq = 'TAC'
    y_seq = 'ACG'
    seq = Sequences(x_seq, y_seq)
    result = arrow.create_seq(seq)
    assert result.x == x_seq[x_start - 1]
    assert result.y == y_seq[y_start - 1]
