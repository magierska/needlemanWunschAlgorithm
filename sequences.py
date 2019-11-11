class Sequences:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def init_from_files(cls, conf):
        x = cls.read_from_file(conf.a)
        y = cls.read_from_file(conf.b)
        return cls(x, y)

    @classmethod
    def read_from_file(cls, file):
        f = open(file)
        x_array = f.readlines()[1:]
        f.close()
        return "".join(x_array)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "\n" + str(self.x) + "\n" + str(self.y) + "\n"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def add(self, sequences):
        return Sequences(self.x + sequences.x, self.y + sequences.y)

    def reverse(self):
        return Sequences(self.x[::-1], self.y[::-1])

    def validate_length(self, max_len):
        if len(self.x) > max_len or len(self.y) > max_len:
            raise ValueError("Sequences shouldn't be longer than " + str(max_len))
