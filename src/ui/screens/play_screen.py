"""
Program name: play_screen
Description: displays the play screen of minesweeper
Inputs: screen and number of mines
Outputs: makes a 10x10 grid with labels and a mine count
External sources: None
Authors: Ruth, Ben, Will
Creation date: 28 August 2025
"""
import pygame as pg
from ...game.settings import WHITE, BLACK
from ...model.board import make_grid, make_labels
import random as rd

class PlayScreen:
    def __init__(self, screen, num_mines, app):
        self.screen = screen
        self.num_mines = num_mines
        self.flags_left = num_mines
        self.font = pg.font.Font(None, 74)
        self.small_font = pg.font.Font(None, 36)
        self.grid = []
        self.play_state = "initial"
        self.remaining_cells = 100 - num_mines  # Total cells minus mines
        self.app = app
        self.loss = False
    # Draw the play screen, updating the display
    def draw(self):
        if self.play_state == "initial":
            self.screen.fill(WHITE)
            self.grid = make_grid()
            make_labels()
        elif self.play_state == "playing":
            self.screen.fill(WHITE)
            make_labels()
            for cell in self.grid:
                cell.draw(self.screen, cell.rect.x, cell.rect.y)
            if self.loss:
                self.play_state = "game_over"
        mines_surface = self.small_font.render(f"Mines Left: {self.flags_left}", True, BLACK)
        self.screen.blit(mines_surface, (57, 490))

        pg.display.update()

    #gets adjacent indices of a cell, accounting for edge cases
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
    
    # Randomly place mines on the grid and update adjacent mine counts  
    def set_mines(self, safe_cell):
        safe_grid = self.grid.copy()
        safe_grid.remove(safe_cell)
        for i in range(self.num_mines):
            target_cell = rd.choice(safe_grid)
            while target_cell.is_mine:
                target_cell = rd.choice(safe_grid)
            target_cell.set_mine()
            #increment adjacent mine counts
            adjacent_indices = self.adjacent_indices(target_cell)
            for index in adjacent_indices:
                if 0 <= index < len(self.grid):
                    self.grid[index].increment_adjacent_mines()

    # Recursively uncover adjacent cells if they have zero adjacent mines
    def uncover_adjacent_cells(self, cell, grid):
        if cell.adjacent_mines == 0 and not cell.is_mine:
            adjacent_indices = self.adjacent_indices(cell)
            for index in adjacent_indices:
                if 0 <= index < len(grid):
                    adjacent_cell = grid[index]
                    if adjacent_cell.is_covered and not adjacent_cell.is_mine:
                        adjacent_cell.uncover()
                        self.remaining_cells -= 1
                        self.uncover_adjacent_cells(adjacent_cell, grid)
    def end_game(self):
        print("got to end game")
        if hasattr(self, 'app') and self.app: #Check to make sure app exists as a good practice
            print("had app")
            self.app.transition_to_game_over() #Call the transition_to_play method in GameApp with the selected number of mines

    # Handle mouse events for uncovering and flagging cells

    GAME_OVER_EVENT = pg.USEREVENT + 1  # event for the game over, to delay the end transition to watch the mines appear
    
    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.play_state == "initial":
                self.play_state = "playing"
                for cell in self.grid:
                    if cell.rect.collidepoint(event.pos):
                        self.set_mines(cell)
        for cell in self.grid:
            if cell.handle_event(event):
                if cell.is_mine and not cell.is_flagged: #Need to make sure the cell isn't already flagged
                    self.loss = True
                    for cell in self.grid:
                        if cell.is_mine:
                            cell.uncover()
                    pg.time.set_timer(self.GAME_OVER_EVENT, 1000, loops=1)  # Set a timer to trigger GAME_OVER_EVENT after 1 second,
                    #the reason for the delay is to allow the player to see the mines before transitioning to game over screen  
                else:
                    self.remaining_cells -= 1
                    self.uncover_adjacent_cells(cell, self.grid)
                    print(f"Cell at index {self.grid.index(cell)} uncovered with {cell.adjacent_mines} adjacent mines. {self.remaining_cells} cells remaining.")
                if self.remaining_cells == 0:
                    print("You Win!")
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
            for cell in self.grid:
                if cell.rect.collidepoint(event.pos):
                    if cell.is_flagged:
                        if self.flags_left > 0:
                            #place a flag and update counter
                            self.flags_left -= 1
                        else:
                            #no more flags left
                            print("No flags left")
                            cell.toggle_flag()
                    else:
                        #remove flag and add one back to the counter
                        self.flags_left += 1
                    
        if event.type == self.GAME_OVER_EVENT:
            self.end_game()