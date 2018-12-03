

class PuzzleReader():

    @staticmethod
    def read_as_list(filepath):
        """Reads in the contents of a .txt file split by newlines. 

        Args:
            filepath (str): Filepath of the puzzle input.
        
        Returns:
            list of str: The contents of the file.
        """
        puzzle_input = []
        with open(filepath) as f:
            puzzle_input = f.readlines()
        return [x.strip() for x in puzzle_input if x != "\n"]