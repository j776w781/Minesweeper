"""
Program name: play_screen
Description: displays the play screen of minesweeper
Inputs: screen and number of mines
Outputs: makes a 10x10 grid with labels and a mine count
External sources: None
Authors: Ruth, Ben, Will, MJ
Creation date: 28 August 2025
"""

#imports
import pygame as pg
from ...game.settings import WHITE, BLACK
from ...model.board import make_grid, make_labels
import random as rd
from copy import deepcopy
import time

#PlayScreen class
#uses board.py and cell.py to draw and play minesweeper
class PlayScreen:
    #variables used in PlayScreen
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
        self.winning_player = 'human'
        self.losing_player = 'human'
        self.board_cleared = False
        self.end_grid = []
        self.instructions = pg.font.Font(None,28).render(f"Left Click to Uncover, Right Click to Flag", True, BLACK)
        self.instructions_2 = pg.font.Font(None,28).render(f"Numbers Indicate Adjacent Mines", True, BLACK)
        self.instructions_3 = pg.font.Font(None,28).render(f"Uncover All Cells and Flag All Mines to Win!", True, BLACK)
    # Draw the play screen, updating the display
    def draw(self):
        #draw the grid, add labels, and make the board ready for user to play
        if self.play_state == "initial":
            self.screen.fill(WHITE)
            self.grid = make_grid()
            make_labels()
            gamestate_surface = self.small_font.render(f"Ready", True, BLACK) #Label to indicate game is ready to play
        #game is being played
        #keep labels and update cells as user interacts with the board
        elif self.play_state == "playing":
            gamestate_surface = self.small_font.render(f"Playing", True, BLACK) #Label to indicate the game is playing
            self.screen.fill(WHITE)
            make_labels()
            for cell in self.grid:
                cell.draw(self.screen, cell.rect.x, cell.rect.y)
        #game is over
        #let's user see board with mines before going to appropriate game over screen(either win or lose)
        elif self.play_state == "game_over":
            #if mine is hit and user loses the game
            if self.loss:
                if self.losing_player == 'human':
                    gamestate_surface = self.small_font.render("You lose!", True, BLACK) #Label to indicate loss
                else:
                    gamestate_surface = self.small_font.render("AI loses!", True, BLACK) #Label to indicate loss

                self.screen.fill(WHITE)
                make_labels()
                for cell in self.end_grid:
                    cell.draw(self.screen, cell.rect.x, cell.rect.y)
            #if user wins the game by revealing everything except mines
            else:
                if self.winning_player == 'human':
                    gamestate_surface = self.small_font.render("You win!", True, BLACK) #Label to indicate victory
                else:
                    gamestate_surface = self.small_font.render("AI wins!", True, BLACK) #Label to indicate loss

                self.screen.fill(WHITE)
                make_labels()
                for cell in self.grid:
                    cell.draw(self.screen, cell.rect.x, cell.rect.y)
        #flag count/mines left label
        mines_surface = self.small_font.render(f"Mines Left: {self.flags_left}", True, BLACK)
        self.screen.blit(mines_surface, (57, 490))
        self.screen.blit(gamestate_surface, (30, 30)) #Draw game_state label
        self.screen.blit(self.instructions, (57, 510)) #Draw instructions label
        self.screen.blit(self.instructions_2, (57, 530)) #Draw instructions label
        self.screen.blit(self.instructions_3, (57, 550)) #Draw instructions label
        #update the display
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
        safe_grid = self.grid.copy() #make a copy of the grid to keep track of safe cells
        safe_grid.remove(safe_cell) #remove the safe cell from the list of cells that can have mines
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
            if cell.is_flagged == True: #if cell is flagged, do not unflag it
                return 
            adjacent_indices = self.adjacent_indices(cell) #get the indices of adjacent cells
            for index in adjacent_indices: 
                if 0 <= index < len(grid): #check if index is valid
                    adjacent_cell = grid[index] #get the adjacent cell 
                    if adjacent_cell.is_covered and not adjacent_cell.is_mine: 
                        adjacent_cell.uncover()
                        self.remaining_cells -= 1
                        self.uncover_adjacent_cells(adjacent_cell, grid)
    def end_game(self):
        print("got to end game")
        '''
        Slight tweaks to this function greatly reduce the code needed in the AISolver methods.
        '''

        '''
        Re-evaluating the timing makes this addition no longer necessary.
        '''
        #self.draw()
        #time.sleep(1)
        if hasattr(self, 'app') and self.app: #Check to make sure app exists as a good practice
            print("had app")
            if self.loss:
                #print("HERE")
                self.app.transition_to_game_over() #Switch to the game over screen
            else:
                self.app.transition_to_victory() #Switch to the victory screen

    # Handle mouse events for uncovering and flagging cells

    GAME_OVER_EVENT = pg.USEREVENT + 1  # event for the game over, to delay the end transition to watch the mines appear
    
    def handle_event(self, event):
        #when user clicks the board for the first time, game goes from "initial" to "playing"
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.play_state == "initial":
                self.play_state = "playing"
                for cell in self.grid:
                    if cell.rect.collidepoint(event.pos):
                        self.set_mines(cell) #set mines after the first click to keep begining safe
        for cell in self.grid:
            if cell.handle_event(event):
                #if mine was revealed and not flagged
                if cell.is_mine and not cell.is_flagged: #Need to make sure the cell isn't already flagged
                    print("BOOM")
                    self.loss = True #user loses game
                    self.losing_player = self.app.player
                    for cell in self.grid:
                        #if the cell is a mine reveal to show user all mines
                        if cell.is_mine:
                            print("Uncover")
                            cell.uncover(override=True)
                    if self.play_state != "game_over": #If the play_state is not already game_over
                        self.end_grid = deepcopy(self.grid) # Store the current grid state for end game display
                    self.play_state = "game_over"
                    pg.time.set_timer(self.GAME_OVER_EVENT, 1000, loops=1)  # Set a timer to trigger GAME_OVER_EVENT after 1 second,
                    #the reason for the delay is to allow the player to see the mines before transitioning to game over screen  
                #reveal cells that are not mines
                else:
                    self.remaining_cells -= 1
                    self.uncover_adjacent_cells(cell, self.grid)
                    print(f"Cell at index {self.grid.index(cell)} uncovered with {cell.adjacent_mines} adjacent mines. {self.remaining_cells} cells remaining.")
                #if all mines are flagged and all other cells revealed, game won
                if self.remaining_cells == 0:
                    print("Game cleared!")
                    self.play_state = "game_over" #Set the play_state to game_over
                    self.winning_player = self.app.player
                    pg.time.set_timer(self.GAME_OVER_EVENT, 1000, loops=1) #Set a timer to trigger GAME_OVER_EVENT after 1 sec
                    self.board_cleared = True #If the # of uncleared, non-mine cells is 0, set this flag to true
            # We check here for the human's mouse click input when an AI has been initialized.

                '''
                After I fixed the lingering start screen problem, I found that I couldn't replay in interactive mode anymore.
                It turned out this block of code was changing the app state back to ai play, even after a losing or winning move.

                Updated the predicate to compensate.
                '''
                if self.app.player == 'human' and self.app.ai != None and not self.loss and not self.board_cleared:
                    self.app.player = 'ai' # For interactive mode we set the player back to 'ai'
                    self.app.state = 'ai play' # For interactive mode we set the state back to 'ai play'

        #checks if user right clicks (add flag) and adjust the flag count           
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
            for cell in self.grid:
                if cell.rect.collidepoint(event.pos):
                    #if the user just placed a flag
                    if cell.is_flagged:
                        if self.play_state == "initial":
                            cell.toggle_flag() #does not let user place flag until play state in "playing"
                            self.flags_left += 1 #fix flag count to keep at 10 before game
                        #if the flag counter is greater than 0 (more flags can be placed)
                        if self.flags_left > 0:
                            #place a flag and update counter
                            self.flags_left -= 1
                            if self.flags_left == 0 and self.board_cleared: #If the number of flags left is 0 AND the board is cleared
                                self.play_state = "game_over"
                                pg.time.set_timer(self.GAME_OVER_EVENT, 1000, loops=1)  # Set a timer to trigger GAME_OVER_EVENT after 1 second
                        #all flags are placed, prevent the user from adding more flags
                        else:
                            #no more flags left
                            print("No flags left")
                            cell.toggle_flag() #remove the flag as soon as it is placed, will look like flag is never placed
                    #if user is removing a flag
                    else:
                        #cell.py takes care of flag removal, so just update flag counter
                        self.flags_left += 1
                    if not cell.is_covered: #if cell is already uncovered
                        self.flags_left -= 1 #remove a counter to keep it at true flag count
                    
        if event.type == self.GAME_OVER_EVENT:
            self.end_game()