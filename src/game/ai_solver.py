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
        #This attribute is no longer necessary.
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
        # This function should only be responsible for making a single move, not UI displays.
        #screen.draw()


        '''
        PlayScreen's handler already accounts for the first click, so this code should be unnecessary.

        # If this is the first move, we need to make a default move because no mines have been set.
        if self.firstMove:
            new_event = pg.event.Event(pg.MOUSEBUTTONDOWN, {'button': 1, 'pos': (75, 110)})
            screen.handle_event(new_event)
            self.firstMove = False
            return
        '''

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

        '''
        The PlayScreen handler does win/loss checking already. I applied a minor tweak to the PlayScreen's end_game() method 
        so that this printing wouldn't be necessary.

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
        '''
        
        # We then wait a second between each move.
        # This function shouldn't be concerned with timing. Let App handle that.
        #time.sleep(1)

    def mediumMode(self, screen):
        self.legalMoves = []
        for i in range(0, 100):
            self.legalMoves.append(i)

        # This function should only be responsible for making a single move, not UI displays.
        #screen.draw()


        '''
        # If this is the first move, we need to make a default move because no mines have been set.
        if self.firstMove:
            new_event = pg.event.Event(pg.MOUSEBUTTONDOWN, {'button': 1, 'pos': (75, 110)})
            screen.handle_event(new_event)
            self.firstMove = False
            return
        '''

        # We will iterate through the entire board looking for obvious bomb locations.
        bomb_spaces = []
        for cell in screen.grid:
            neighbors = []
            if not cell.is_covered:
                initial_adjacents = screen.adjacent_indices(cell)
                surroundings = []
                # Next is an awesome detour because the adjacent_indices method doesn't consider corner cases!
                for index in initial_adjacents:
                    if index in range(0, 100):
                        surroundings.append(index)
                for neighbor in surroundings:
                    if screen.grid[neighbor].is_covered:
                        neighbors.append(neighbor)
                if len(neighbors) == cell.adjacent_mines:
                    for neighbor in neighbors:
                        if neighbor not in bomb_spaces:
                            bomb_spaces.append(neighbor)
        
        # Now we will iterate through the entire board again looking for moves the AI can prioritize.
        priority_moves = []
        for cell in screen.grid:
            neighbors = []
            if not cell.is_covered:
                # One refresher on list comprehension later and...
                neighbors = [
                        index for index in screen.adjacent_indices(cell) 
                        if index in range (0, 100) and screen.grid[index].is_covered
                ]
                # Check how many mines are in the neighbors.
                neighbor_mines = sum(1 for index in neighbors if index in bomb_spaces)
                # If all mines are accounted for in a space, but there are still more covered cells. Add non-bomb cells.
                if neighbor_mines == cell.adjacent_mines and len(neighbors) > neighbor_mines:
                    for neighbor in neighbors:
                        if neighbor not in bomb_spaces:
                            priority_moves.append(neighbor)
                
        # We should now have the locations of all obvious bombs.
        # So it's time to find our legal moves!
        if len(priority_moves) == 0:
            for index in range(len(screen.grid)):
                if index in bomb_spaces: # Cell is a mine!
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
        else:
            move = random.choice(priority_moves) # Pick a move at random (because why not?)
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

        '''
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
        '''
        
        # We then wait a second between each move.
        # This function shouldn't be concerned with timing. Let App handle that.
        #time.sleep(1)




    def hardMode(self, screen):
        # We want to define all legal moves that the AI could make.
        self.legalMoves = []
        for i in range(0, 100):
            self.legalMoves.append(i)

        # Now draw the screen.
        # This function should only be responsible for making a single move, not UI displays.
        #screen.draw()


        '''
        # If this is the first move, we need to make a default move because no mines have been set.
        if self.firstMove:
            new_event = pg.event.Event(pg.MOUSEBUTTONDOWN, {'button': 1, 'pos': (75, 110)})
            screen.handle_event(new_event)
            self.firstMove = False
            return
        '''

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

        '''
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
        '''
        
        # We then wait a second between each move.
        # This function shouldn't be concerned with timing. Let App handle that.
        #time.sleep(1)

