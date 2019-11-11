from arrow import Arrow
from sequences import Sequences


class UpArrow(Arrow):
    def __eq__(self, other):
        return isinstance(other, UpArrow) and self.eq(other)

    def create_seq(self, sequences):
        return Sequences("-", sequences.y[self.start.y - 1])
