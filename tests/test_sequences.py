import pytest
from sequences import Sequences


def test_add():
    seq1 = Sequences('A', 'BC')
    seq2 = Sequences('DE', 'F')
    result = seq1.add(seq2)
    assert result == Sequences(seq1.x + seq2.x, seq1.y + seq2.y)


def test_reverse():
    seq = Sequences('ABC', 'DEF')
    result = seq.reverse()
    assert result == Sequences('CBA', 'FED')


def test_validate_length():
    seq = Sequences('A', 'BC')
    with pytest.raises(ValueError):
        seq.validate_length(1)
