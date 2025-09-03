"""
Program name: play_screen
Description: displays the play screen of minesweeper
Inputs: screen and number of mines
Outputs: makes a 10x19 grid with labels and a mine count
External sources:
Authors: Ruth Higgason
Creation date: 28 August 2025
"""
import pygame as pg
from ...game.settings import WHITE, BLACK
from ...model.board import make_grid

class PlayScreen:
    def __init__(self, screen, num_mines):
        self.screen = screen
        self.num_mines = num_mines
        self.font = pg.font.Font(None, 74)
        self.small_font = pg.font.Font(None, 36)
        self.grid = make_grid()

    def draw(self):
        self.screen.fill(WHITE)
        make_grid()

        mines_surface = self.small_font.render(f"Mines: {self.num_mines}", True, BLACK)
        self.screen.blit(mines_surface, (525, 100))

        pg.display.update()


    def handle_event(self, event):
        #for when cells are clicked
        pass