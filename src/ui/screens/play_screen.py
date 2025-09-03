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

    def adjacent_indices(self, cell):
        target_index = self.grid.index(cell)
        left_edge = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
        right_edge = [9, 19, 29, 39, 49, 59, 69, 79, 89, 99]
        if (target_index in left_edge):
            return [target_index + 1, target_index + 10, target_index + 11, target_index - 9, target_index - 10]
        elif (target_index in right_edge):
            return [target_index - 1, target_index + 10, target_index + 9, target_index - 11, target_index - 10]
        else:
            return [target_index - 1, target_index + 1, target_index + 10, target_index - 10, target_index + 9, target_index + 11, target_index - 9, target_index - 11]
    
    def set_mines(self):
        for i in range(self.num_mines):
            target_cell = rd.choice(self.grid)
            while target_cell.is_mine:
                target_cell = rd.choice(self.grid)
            target_cell.set_mine()
            #increment adjacent mine counts
            adjacent_indices = self.adjacent_indices(target_cell)
            for index in adjacent_indices:
                if 0 <= index < len(self.grid):
                    self.grid[index].increment_adjacent_mines()

    def uncover_adjacent_cells(self, cell, grid):
        if cell.adjacent_mines == 0 and not cell.is_mine:
            adjacent_indices = self.adjacent_indices(cell)
            for index in adjacent_indices:
                if 0 <= index < len(grid):
                    adjacent_cell = grid[index]
                    if adjacent_cell.is_covered and not adjacent_cell.is_mine:
                        adjacent_cell.uncover()
                        self.uncover_adjacent_cells(adjacent_cell, grid)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.play_state == "initial":
                self.play_state = "playing"
                self.set_mines()
        for cell in self.grid:
            if cell.handle_event(event):
                #if cell.is_mine:
                #   self.play_state = "game_over"
                #  print("Game Over")
                #else:
                self.uncover_adjacent_cells(cell, self.grid)
                print(f"Cell at index {self.grid.index(cell)} uncovered with {cell.adjacent_mines} adjacent mines.")