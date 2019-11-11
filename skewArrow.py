from arrow import Arrow
from sequences import Sequences


class SkewArrow(Arrow):
    def __eq__(self, other):
        return isinstance(other, SkewArrow) and self.eq(other)

    def create_seq(self, sequences):
        return Sequences(sequences.x[self.start.x - 1], sequences.y[self.start.y - 1])
