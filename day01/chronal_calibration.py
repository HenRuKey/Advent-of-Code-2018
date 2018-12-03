import sys
from itertools import cycle
# Import PuzzleReader to get the contents of the puzzle input file.
sys.path.append('../')
from puzzle_reader import PuzzleReader

class Calibrator():
    """A class to read-in and store frequency changes.

    Args:
        puzzle_filepath (str): The filepath of the puzzle input.
    """

    def __init__(self, puzzle_filepath):
        self.freq_changes = [int(x) for x in PuzzleReader.read_as_list(puzzle_filepath)]

    @property
    def ResultingFrequency(self):
        """The sum of all frequency changes read from the puzzle file."""
        return sum(self.freq_changes)

    @property
    def FirstRepeatingFrequency(self):
        """The first frequency that is reached twice during repeated frequency shifts."""
        prev_freqs = {0}
        freq = 0
        for offset in cycle(self.freq_changes):
            freq += offset
            if freq in prev_freqs:
                return freq
            else:
                prev_freqs.add(freq)
            
if __name__ == "__main__":
    # Gets filename from console args if present, otherwise uses default path.
    filename = ""
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "day01_puzzle_input.txt"
    # Creates an instance of Calibrator.
    calibrator = Calibrator(filename)
    # Displays solutions to the console.
    print("Resulting Frequency: {}".format(calibrator.ResultingFrequency))
    print("Repeating Frequency: {}".format(calibrator.FirstRepeatingFrequency))