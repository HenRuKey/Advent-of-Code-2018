import sys
import collections
from difflib import SequenceMatcher
# Import PuzzleReader to get the contents of the puzzle input file.
sys.path.append('../')
from puzzle_reader import PuzzleReader


class InventoryManager():
    """A class to store inventory and calculate Checksum.

    Args:
        puzzle_filepath (str): The filepath of the puzzle input.
    """
    
    def __init__(self, puzzle_filepath):
        self.inventory = PuzzleReader.read_as_list(puzzle_filepath)

    @staticmethod
    def find_hamming_distance(id1, id2):
        """"Finds the number of chars that are not in common between two strings."""
        if (len(id1) != len(id2)):
            raise ValueError("The length of the ids do not match.")
        return sum(el1 != el2 for el1, el2 in zip(id1, id2))

    @property 
    def Checksum(self):
        """The number of IDs with 3 repeating characters multiplied by the number of IDs with 2 repeating characters."""
        two_items = 0
        three_items = 0
        for item_id in self.inventory:
            two_items += 1 if (len([char for char, count in collections.Counter(item_id).items() if count == 2]) > 0) else 0
            three_items += 1 if (len([char for char, count in collections.Counter(item_id).items() if count == 3]) > 0) else 0
        return two_items * three_items

    @property
    def CommonLetters(self):
        """The chars in common between two ids with the most overlap."""
        for index, item_id in enumerate(self.inventory):
            for x in range(index+1, len(self.inventory)):
                other_id = self.inventory[x]
                if InventoryManager.find_hamming_distance(item_id, other_id) == 1:
                    overlap = [char for num, char in enumerate(item_id) if char == other_id[num]]
                    return ''.join(overlap)
                



if __name__ == "__main__":
    # Gets filename from console args if present, otherwise uses default path.
    filename = ""
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "day02_puzzle_input.txt"
    # Creates an instance of InventoryManager.
    manager = InventoryManager(filename)
    # Displays solutions to the console.
    print("Checksum: {}".format(manager.Checksum))
    print("Common Letters: {}".format(manager.CommonLetters))