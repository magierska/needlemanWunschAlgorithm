from configuration import Configuration
from sequences import Sequences
from sequenceAlignment import SequenceAlignment
from point import Point
from skewArrow import  SkewArrow
from upArrow import UpArrow
from leftArrow import LeftArrow

def test_follow_arrows():
    conf = Configuration(5, -5, -2, 2, 15)
    seq_alignment = SequenceAlignment(conf)

    sequences = Sequences('SUM', 'SAM')
    x_len = len(sequences.x)
    y_len = len(sequences.y)
    seq_alignment.sequences = sequences

    arrows = [SkewArrow(1, 1, 0, 0), LeftArrow(2, 1, 1, 1), LeftArrow(3, 1, 2, 1), UpArrow(1, 2, 1, 1),
              UpArrow(2, 2, 2, 1), LeftArrow(2, 2, 1, 2), UpArrow(3, 2, 3, 1), LeftArrow(3, 2, 2, 2),
              UpArrow(1, 3, 1, 2), UpArrow(2, 3, 2, 2), LeftArrow(2, 3, 1, 3), SkewArrow(3, 3, 2, 2)]
    arrows += [LeftArrow(i + 1, 0, i, 0) for i in range(x_len)]
    arrows += [UpArrow(0, i + 1, 0, i) for i in range(y_len)]
    seq_alignment.arrows = arrows

    result = seq_alignment.follow_arrows(Point(x_len, y_len), Sequences('', ''))
    exp_result = [Sequences('M-US', 'MA-S'), Sequences('MU-S', 'M-AS')]
    assert len(result) == len(exp_result)
    for exp_seq in exp_result:
        assert any([seq == exp_seq for seq in result])


