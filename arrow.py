from point import Point


class Arrow:
    def __init__(self, x_start, y_start, x_end, y_end):
        self.start = Point(x_start, y_start)
        self.end = Point(x_end, y_end)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "From: " + str(self.start) + " to: " + str(self.end)

    def __eq__(self, other):
        return isinstance(other, Arrow) and self.eq(other)

    def eq(self, other):
        return self.start == other.start and self.end == other.end

    def create_seq(self, seq_x, seq_y):
        raise NotImplementedError
