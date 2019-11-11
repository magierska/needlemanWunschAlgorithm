import argparse


class Arguments:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-a", type=str, help="Path to first sequence", required=True)
        parser.add_argument("-b", type=str, help="Path to second sequence", required=True)
        parser.add_argument("-c", type=str, help="Path to config file", required=True)
        parser.add_argument("-o", type=str, help="Path to output file", required=True)
        args = parser.parse_args()
        self.a = args.a
        self.b = args.b
        self.c = args.c
        self.o = args.o
