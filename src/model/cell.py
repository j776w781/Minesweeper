#cell will be a class and it will have types of covered, flagged, and uncovered
import pygame as pg

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
    #draw will draw the cell on the screen, depending on the cell's state
    def draw(self, surface, x, y):
        rect = pg.Rect(x, y, 20, 20)
        if self.is_covered: #covered cell drawing
            pg.draw.rect(surface, (200, 200, 200), rect, width=0, border_radius=2)
            if self.is_flagged:
                pg.draw.circle(surface, (255, 0, 0), rect.center, 5)
        else: #uncovered cell drawing
            pg.draw.rect(surface, (150, 150, 150), rect, width=0, border_radius=2)
            if self.is_mine:
                pg.draw.circle(surface, (0, 0, 0), rect.center, 5)
            elif self.adjacent_mines > 0:
                font = pg.font.Font(None, 24)
                text_surface = font.render(str(self.adjacent_mines), True, (0, 0, 255))
                text_rect = text_surface.get_rect(center=rect.center)
                surface.blit(text_surface, text_rect)