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
import random as rd

class PlayScreen:
    def __init__(self, screen, num_mines):
        self.screen = screen
        self.num_mines = num_mines
        self.font = pg.font.Font(None, 74)
        self.small_font = pg.font.Font(None, 36)
        self.grid = []
        self.play_state = "initial"

    def draw(self):
        if self.play_state == "initial":
            self.screen.fill(WHITE)
            self.grid = make_grid()
        elif self.play_state == "playing":
            for cell in self.grid:
                cell.draw(self.screen, cell.rect.x, cell.rect.y)

        mines_surface = self.small_font.render(f"Mines: {self.num_mines}", True, BLACK)
        self.screen.blit(mines_surface, (525, 100))

        pg.display.update()

    def set_mines(self):
        for i in range(self.num_mines):
            target_cell = rd.choice(self.grid)
            while target_cell.is_mine:
                target_cell = rd.choice(self.grid)
            target_cell.set_mine()
            #increment adjacent mine counts

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.play_state == "initial":
                self.play_state = "playing"
                self.set_mines()
        for cell in self.grid:
            cell.handle_event(event)