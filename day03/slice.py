import sys
# Import PuzzleReader to get the contents of the puzzle input file.
sys.path.append('../')
from puzzle_reader import PuzzleReader

class Claim():
    """A definition for coordinates covering a plane.

    Args:
        id (int): The id of the claim.
        distance_left (int): The number of inches to the left edge of the plane.
        distance_top (int): The number of inches to the top edge of the plane.
        width (int): Total width of the claim in inches.
        height (int): Total height of the claim in inches.
    """

    def __init__(self, id, distance_left, distance_top, width, height):
        self._id = id
        self._distance_left = distance_left
        self._distance_top = distance_top
        self._width = width
        self._height = height
        self._coordinates = None

    def find_coordinates(self):
        """Identifies all the coordinates that exist in the claim."""
        coordinates = []
        x_coordinates = [x for x in range(self._distance_left, self._width + self._distance_left)]
        y_coordinates = [y for y in range(self._distance_top, self._height + self._distance_top)]
        for x in x_coordinates:
            coordinates += [(x,y) for y in y_coordinates]
        return coordinates

    @property
    def id(self):
        """The claim's ID."""
        return self._id

    @property
    def coordinates(self):
        """All the coordinates that exist in the claim."""
        if self._coordinates is None:
            self._coordinates = self.find_coordinates()
        return self._coordinates

class Slicer():
    """A claim manager.

    Args:
        puzzle_filepath (str): The path to the puzzle input file.
    """

    def __init__(self, puzzle_filepath):
        self.puzzle_input = PuzzleReader.read_as_list(puzzle_filepath)
        self.claims = self.parse_claims_from_list(self.puzzle_input)

    @property
    def unique_claim(self):
        """A single claim that has no overlap with any other claim."""
        overlap = self.overlap
        for claim in self.claims:
            has_overlap = False
            for coord in claim.coordinates:
                if coord in overlap:
                    has_overlap = True
                    break
            if not has_overlap:
                return claim

    @property
    def overlap(self):
        """All coordinates that exist in more than one claim."""
        seen = set({})
        overlapped = set({})
        for claim in self.claims:
            for coord in claim.coordinates:
                if coord not in seen:
                    seen.add(coord)
                elif coord in seen and coord not in overlapped:
                    overlapped.add(coord)
        return overlapped


    def parse_claims_from_list(self, puzzle_input):
        """Parses claim data from a list of plain strings.

        Args:
            puzzle_input (list of str): The puzzle input.
        
        Returns:
            list of Claims: A collection of claims.
        """
        claims = []
        for value in puzzle_input:
            value = value.split(' ')
            claims.append(Claim(
                id=int(value[0].replace('#', '')),
                distance_left=int(value[2].split(',')[0]),
                distance_top=int(value[2].split(',')[1].replace(':','')),
                width=int(value[3].split('x')[0]),
                height=int(value[3].split('x')[1])
            ))
        return claims
        

if __name__ == "__main__":
    # Gets filename from console args if present, otherwise uses default path.
    filename = ""
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "day03_puzzle_input.txt"
    # Create a new instance of Slicer
    slicer = Slicer(filename)
    # Display the results.
    print("Number of overlapping coordinates: {}".format(len(slicer.overlap)))
    print("Unique claim: {}".format(slicer.unique_claim.id))