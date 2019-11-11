from upArrow import UpArrow
from sequences import Sequences


def test_create_seq():
    y_start = 2
    arrow = UpArrow(1, y_start, 1, y_start - 1)
    y_seq = 'ACG'
    seq = Sequences('TAC', y_seq)
    result = arrow.create_seq(seq)
    assert result.x == '-'
    assert result.y == y_seq[y_start - 1]
