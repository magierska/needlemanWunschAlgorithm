from sequenceAlignment import SequenceAlignment
from sequences import Sequences
from arguments import Arguments
from outputCreator import OutputCreator
from configuration import Configuration

try:
    arguments = Arguments()
    conf = Configuration.init_from_file(arguments.c)

    seq_alignment = SequenceAlignment(conf)
    result = seq_alignment.find(Sequences.init_from_files(arguments))

    output_creator = OutputCreator(arguments.o)
    output_creator.write(result)

    print("Calculation finished. Result saved in: " + arguments.o)
except ValueError as e:
    print("Error: " + str(e))
except:
    print("Something went wrong. Please contact administrator.")
