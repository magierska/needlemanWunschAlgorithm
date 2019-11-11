import numpy as np
from upArrow import UpArrow
from leftArrow import LeftArrow
from skewArrow import SkewArrow


class MatrixCreator:
    def __init__(self, conf):
        self.conf = conf
        self.arrows = []

    def prepare_base_values_matrix(self, x_len, y_len):
        values_matrix = np.zeros((y_len + 1, x_len + 1))

        for i in range(y_len):
            values_matrix[i + 1][0] = (i + 1) * self.conf.gap
            self.arrows.append(UpArrow(0, i + 1, 0, i))

        for i in range(x_len):
            values_matrix[0][i + 1] = (i + 1) * self.conf.gap
            self.arrows.append(LeftArrow(i + 1, 0, i, 0))

        return values_matrix

    def down(self, values_matrix, i, j):
        return values_matrix[i - 1][j] + self.conf.gap, UpArrow(j, i, j, i - 1)

    def right(self, values_matrix, i, j):
        return values_matrix[i][j - 1] + self.conf.gap, LeftArrow(j, i, j - 1, i)

    def skew(self, values_matrix, i, j):
        val = self.conf.same if self.sequences.y[i - 1] == self.sequences.x[j - 1] else self.conf.diff
        return values_matrix[i - 1][j - 1] + val, SkewArrow(j, i, j - 1, i - 1)

    def make_next_step(self, values_matrix, i, j):
        down_val, down_arr = self.down(values_matrix, i, j)
        right_val, right_arr = self.right(values_matrix, i, j)
        skew_val, skew_arr = self.skew(values_matrix, i, j)
        max_val = max(down_val, right_val, skew_val)
        if max_val == down_val:
            self.arrows.append(down_arr)
        if max_val == right_val:
            self.arrows.append(right_arr)
        if max_val == skew_val:
            self.arrows.append(skew_arr)

        return max_val

    def prepare_result_and_arrows(self, sequences):
        self.sequences = sequences
        x_len = len(self.sequences.x)
        y_len = len(self.sequences.y)

        values_matrix = self.prepare_base_values_matrix(x_len, y_len)

        for i in range(1, y_len + 1):
            for j in range(1, x_len + 1):
                values_matrix[i, j] = self.make_next_step(values_matrix, i, j)

        return self.arrows, values_matrix[y_len, x_len]
