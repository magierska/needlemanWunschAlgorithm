from matrixCreator import MatrixCreator
from configuration import Configuration
from leftArrow import LeftArrow
from upArrow import UpArrow
from skewArrow import SkewArrow
from sequences import Sequences
import numpy as np


def test_prepare_base_values_matrix():
    conf = Configuration(5, -5, -2, 2, 15)
    matrix = MatrixCreator(conf)
    x_len = 5
    y_len = 6
    result = matrix.prepare_base_values_matrix(x_len, y_len)

    assert result.shape == (y_len + 1, x_len + 1)
    assert len(matrix.arrows) == x_len + y_len
    assert result[0][0] == 0

    for i in range(1, x_len + 1):
        assert result[0][i] == i * conf.gap
        assert any([arr == LeftArrow(i, 0, i - 1, 0) for arr in matrix.arrows])

    for i in range(1, y_len + 1):
        assert result[i][0] == i * conf.gap
        assert any([arr == UpArrow(0, i, 0, i - 1) for arr in matrix.arrows])

    for i in range(1, y_len + 1):
        for j in range(1, x_len + 1):
            assert result[i][j] == 0


def test_down():
    conf = Configuration(5, -5, -2, 2, 15)
    matrix = MatrixCreator(conf)
    values = np.zeros((5, 6))
    i = 3
    j = 3
    value, arrow = matrix.down(values, i, j)
    assert values[i - 1, j] + conf.gap == value
    assert UpArrow(j, i, j, i - 1) == arrow


def test_right():
    conf = Configuration(5, -5, -2, 2, 15)
    matrix = MatrixCreator(conf)
    values = np.zeros((5, 6))
    i = 3
    j = 3
    value, arrow = matrix.right(values, i, j)
    assert values[i, j - 1] + conf.gap == value
    assert LeftArrow(j, i, j - 1, i) == arrow


def test_skew_same():
    conf = Configuration(5, -5, -2, 2, 15)
    matrix = MatrixCreator(conf)
    matrix.sequences = Sequences('TACG', 'GTCAA')
    values = np.zeros((5, 6))
    i = 3
    j = 3
    value, arrow = matrix.skew(values, i, j)
    assert values[i - 1, j - 1] + conf.same == value
    assert SkewArrow(j, i, j - 1, i - 1) == arrow


def test_skew_diff():
    conf = Configuration(5, -5, -2, 2, 15)
    matrix = MatrixCreator(conf)
    matrix.sequences = Sequences('TATG', 'GTCAA')
    values = np.zeros((5, 6))
    i = 3
    j = 3
    value, arrow = matrix.skew(values, i, j)
    assert values[i - 1, j - 1] + conf.diff == value
    assert SkewArrow(j, i, j - 1, i - 1) == arrow


def test_make_next_step_gap():
    conf = Configuration(5, -5, -2, 2, 15)
    matrix = MatrixCreator(conf)
    matrix.sequences = Sequences('TATG', 'GTCAA')
    values = np.zeros((5, 6))
    i = 3
    j = 2
    max_val = matrix.make_next_step(values, i, j)
    assert conf.gap == max_val
    assert len(matrix.arrows) == 2
    assert any([arr == UpArrow(j, i, j, i - 1) for arr in matrix.arrows])
    assert any([arr == LeftArrow(j, i, j - 1, i) for arr in matrix.arrows])


def test_make_next_step_same():
    conf = Configuration(5, -5, -2, 2, 15)
    matrix = MatrixCreator(conf)
    matrix.sequences = Sequences('TATG', 'GCATA')
    values = np.zeros((5, 6))
    i = 3
    j = 2
    max_val = matrix.make_next_step(values, i, j)
    assert conf.same == max_val
    assert len(matrix.arrows) == 1
    assert any([arr == SkewArrow(j, i, j - 1, i - 1) for arr in matrix.arrows])


def test_make_next_step_diff():
    conf = Configuration(5, -5, -2, 2, 15)
    matrix = MatrixCreator(conf)
    matrix.sequences = Sequences('TCTG', 'GCATA')
    values = np.zeros((5, 6))
    i = 3
    j = 2
    values[i - 1][j] = values[i][j-1] = -4
    max_val = matrix.make_next_step(values, i, j)
    assert conf.diff == max_val
    assert len(matrix.arrows) == 1
    assert any([arr == SkewArrow(j, i, j - 1, i - 1) for arr in matrix.arrows])


def test_prepare_result_and_arrows():
    conf = Configuration(5, -5, -2, 2, 15)
    matrix = MatrixCreator(conf)
    sequences = Sequences('SUM', 'SAM')
    arrows, value = matrix.prepare_result_and_arrows(sequences)
    exp_arrows = [SkewArrow(1, 1, 0, 0), LeftArrow(2, 1, 1, 1), LeftArrow(3, 1, 2, 1), UpArrow(1, 2, 1, 1),
                  UpArrow(2, 2, 2, 1), LeftArrow(2, 2, 1, 2), UpArrow(3, 2, 3, 1), LeftArrow(3, 2, 2, 2),
                  UpArrow(1, 3, 1, 2), UpArrow(2, 3, 2, 2), LeftArrow(2, 3, 1, 3), SkewArrow(3, 3, 2, 2)]
    exp_arrows += [LeftArrow(i + 1, 0, i, 0) for i in range(len(sequences.x))]
    exp_arrows += [UpArrow(0, i + 1, 0, i) for i in range(len(sequences.y))]
    for exp_arr in exp_arrows:
        assert any([arr == exp_arr for arr in arrows])
    assert value == 6



