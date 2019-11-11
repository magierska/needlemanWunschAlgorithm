from point import Point
from sequences import Sequences
from matrixCreator import MatrixCreator
from result import Result


class SequenceAlignment:
    def __init__(self, conf):
        self.conf = conf
        self.sequences = {}
        self.arrows = []
        self.count = 0

    def follow_arrows(self, point, sequences):
        if point == Point(0, 0):
            self.count += 1
            return [sequences]

        arrows_from_point = [arrow for arrow in self.arrows if arrow.start == point]
        result = []
        for arrow in arrows_from_point:
            new_sequences = sequences.add(arrow.create_seq(self.sequences))
            seq_arr = self.follow_arrows(arrow.end, new_sequences)
            result += seq_arr
            if self.count == self.conf.max_seq_count:
                return result

        return result

    def find(self, sequences):
        self.sequences = sequences
        self.count = 0
        self.sequences.validate_length(self.conf.max_seq_len)

        matrix_creator = MatrixCreator(self.conf)
        self.arrows, value = matrix_creator.prepare_result_and_arrows(self.sequences)

        result = self.follow_arrows(Point(len(self.sequences.x), len(self.sequences.y)), Sequences("", ""))

        reversed_result = [seq.reverse() for seq in result]

        return Result(reversed_result, value)
