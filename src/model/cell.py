#cell will be a class and it will have types of covered, flagged, and uncovered
class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_covered = True
        self.is_flagged = False
        self.adjacent_mines = 0
    #uncover will uncover the cell if it is not flagged
    def uncover(self):
        if not self.is_flagged:
            self.is_covered = False
    #toggle_flag will toggle the flag on the cell if it is covered
    def toggle_flag(self):
        if self.is_covered:
            self.is_flagged = not self.is_flagged
    #set_mine will set the cell to be a mine
    def set_mine(self):
        self.is_mine = True
    #increment_adjacent_mines will increment the number of adjacent mines
    def increment_adjacent_mines(self):
        self.adjacent_mines += 1