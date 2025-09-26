import pygame as pg
import time
import random
from .settings import WIDTH, HEIGHT, FPS
from ..ui.screens.start_screen import StartScreen
from ..ui.screens.play_screen import PlayScreen
from ..ui.screens.game_over_screen import GameOverScreen
from ..ui.screens.victory_screen import VictoryScreen
from ..input.mouse import InputController
from ..model.cell import Cell

class AiSolver:
    def __init__(self):
        self.firstMove = True
        self.legalMoves = []


    def AIMove(self, screen, difficulty):
        if difficulty == 'easy':
            self.easyMode(screen)
        elif difficulty == 'medium':
            self.mediumMode(screen)
        elif difficulty == 'hard':
            self.hardMode(screen)
        else:
            pass

    def easyMode(self, screen):
        # We define all legal moves     
        self.legalMoves = []
        for i in range(0, 100):
            self.legalMoves.append(i)

        # Now draw the screen.
        screen.draw()

        # If this is the first move, we need to make a default move because no mines have been set.
        if self.firstMove:
            new_event = pg.event.Event(pg.MOUSEBUTTONDOWN, {'button': 1, 'pos': (75, 110)})
            screen.handle_event(new_event)
            self.firstMove = False
            return

         # When we make any generic move, we read the board and remove all illegal moves.
            # These include cells that are uncovered only (because it's easy mode).
        for index in range(len(screen.grid)):
            if not screen.grid[index].is_covered: # Cell is uncovered!
                # Find where in legalMoves that cell is...
                bad_index = self.legalMoves.index(index)
                # Delete it from legalMoves.
                self.legalMoves.pop(bad_index)

        if len(self.legalMoves) != 0: # If there are legalMoves, we should create our input!
            move = random.choice(self.legalMoves) # Pick a move at random (because why not?)
            # We then take that index and convert it to the pixel position of the displayed cell.
            if move > 9:
                move = str(move)
                y = int(move[0])
                x = int(move[1])
            else:
                y = 0
                x = move

            # We use some math to create a mouse click at the box's position.
            new_event = pg.event.Event(pg.MOUSEBUTTONDOWN, {'button': 1, 'pos': (75 + (40*x), 110 + (40*y))})
            # Then we send that mouse click over to the play screen to be handled with the previous group's code.
            screen.handle_event(new_event)

        # We check here for a game win or loss (because for some reason it doesn't work in the previous group's loop)
            # The previous group didn't fail us, but somehow our intervention breaks their game loop.
        if screen.remaining_cells == 0:
            screen.play_state = 'game_over'

        if screen.play_state == 'game_over':
            if screen.loss == True:
                for cell in screen.grid:
                    #if the cell is a mine reveal to show user all mines
                    if cell.is_mine:
                        cell.uncover(override=True)
                screen.draw()
                time.sleep(1)
                screen.end_game()
            else:
                screen.draw()
                time.sleep(1)
                screen.end_game()
        
        # We then wait a second between each move.
        time.sleep(1)

    def mediumMode(self, screen):
        print("Medium mode enabled")
        # These methods read the board and make the best move for that board state.
        # We're not trying to solve the entire board in this method, we just need to find the best logical move.

    def hardMode(self, screen):
        # We want to define all legal moves that the AI could make.
        self.legalMoves = []
        for i in range(0, 100):
            self.legalMoves.append(i)

        # Now draw the screen.
        screen.draw()

        # If this is the first move, we need to make a default move because no mines have been set.
        if self.firstMove:
            new_event = pg.event.Event(pg.MOUSEBUTTONDOWN, {'button': 1, 'pos': (75, 110)})
            screen.handle_event(new_event)
            self.firstMove = False
            return

        # When we make any generic move, we read the board and remove all illegal moves.
            # These include cells that are uncovered, and cells with bombs (for hard mode).
        for index in range(len(screen.grid)):
            if screen.grid[index].is_mine: # Cell is a mine!
                # Find where in legalMoves that mine coordinate is...
                bad_index = self.legalMoves.index(index)
                # ...and delete it from legalMoves.
                self.legalMoves.pop(bad_index)
            elif not screen.grid[index].is_covered: # Cell is uncovered!
                # Find where in legalMoves that cell is...
                bad_index = self.legalMoves.index(index)
                # Delete it from legalMoves.
                self.legalMoves.pop(bad_index)

        if len(self.legalMoves) != 0: # If there are legalMoves, we should create our input!
            move = random.choice(self.legalMoves) # Pick a move at random (because why not?)
            # We then take that index and convert it to the pixel position of the displayed cell.
            if move > 9:
                move = str(move)
                y = int(move[0])
                x = int(move[1])
            else:
                y = 0
                x = move

            # We use some math to create a mouse click at the box's position.
            new_event = pg.event.Event(pg.MOUSEBUTTONDOWN, {'button': 1, 'pos': (75 + (40*x), 110 + (40*y))})
            # Then we send that mouse click over to the play screen to be handled with the previous group's code.
            screen.handle_event(new_event)

        # We check here for a game win or loss (because for some reason it doesn't work in the previous group's loop)
            # The previous group didn't fail us, but somehow our intervention breaks their game loop.
        if screen.remaining_cells == 0:
            screen.play_state = 'game_over'

        if screen.play_state == 'game_over':
            if screen.loss == True:
                for cell in screen.grid:
                    #if the cell is a mine reveal to show user all mines
                    if cell.is_mine:
                        cell.uncover(override=True)
                screen.draw()
                time.sleep(1)
                screen.end_game()
            else:
                screen.draw()
                time.sleep(1)
                screen.end_game()
        
        # We then wait a second between each move.
        time.sleep(1)

