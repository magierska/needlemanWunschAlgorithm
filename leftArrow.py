from arrow import Arrow
from sequences import Sequences


class LeftArrow(Arrow):
    def __eq__(self, other):
        return isinstance(other, LeftArrow) and self.eq(other)

    def create_seq(self, sequences):
        return Sequences(sequences.x[self.start.x - 1], "-")
