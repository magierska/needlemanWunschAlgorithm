class OutputCreator:
    def __init__(self, file):
        self.file = file

    def write(self, result):
        f = open(self.file, 'w+')
        f.write("SCORE = " + str(int(result.score)) + "\n")
        [f.write(str(seq)) for seq in result.sequences]
        f.close()
