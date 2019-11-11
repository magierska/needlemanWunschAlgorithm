import configparser


class Configuration:
    def __init__(self, same, diff, gap, max_seq_count, max_seq_len):
        self.same = same
        self.diff = diff
        self.gap = gap
        self.max_seq_count = max_seq_count
        self.max_seq_len = max_seq_len

    @classmethod
    def init_from_file(cls, config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        try:
            same = int(config['DEFAULT']['SAME'])
            diff = int(config['DEFAULT']['DIFF'])
            gap = int(config['DEFAULT']['GAP_PENALTY'])
            max_seq_count = int(config['DEFAULT']['MAX_NUMBER_PATHS'])
            max_seq_len = int(config['DEFAULT']['MAX_SEQ_LENGTH'])
            return cls(same, diff, gap, max_seq_count, max_seq_len)
        except ValueError:
            raise ValueError('All values in config file should be numbers.')
        except KeyError as e:
            raise ValueError(str(e) + " is missing in config file.")
