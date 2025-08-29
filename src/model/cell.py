#cell will be a class and it will have types of covered, flagged, and uncovered
class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_covered = True
        self.is_flagged = False
        self.adjacent_mines = 0

    def uncover(self):
        if not self.is_flagged:
            self.is_covered = False

    def toggle_flag(self):
        if self.is_covered:
            self.is_flagged = not self.is_flagged

    def set_mine(self):
        self.is_mine = True

    def increment_adjacent_mines(self):
        self.adjacent_mines += 1