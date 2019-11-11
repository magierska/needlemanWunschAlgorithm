from leftArrow import LeftArrow
from sequences import Sequences


def test_create_seq():
    x_start = 2
    arrow = LeftArrow(x_start, 0, x_start - 1, 0)
    x_seq = 'ACG'
    seq = Sequences(x_seq, 'TAC')
    result = arrow.create_seq(seq)
    assert result.x == x_seq[x_start - 1]
    assert result.y == '-'
