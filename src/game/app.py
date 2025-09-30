"""
Program name: app.py
Description: This is the core backend of the program that manages which screen is active
and the transitions between each of the files
Inputs: takes in number of mines from the user
Outputs: prints the screens
External sources: None
Authors: Will, MJ
Creation date: 28 August 2025
"""

import pygame as pg
import time
from .settings import WIDTH, HEIGHT, FPS
from ..ui.screens.start_screen import StartScreen
from ..ui.screens.play_screen import PlayScreen
from ..ui.screens.game_over_screen import GameOverScreen
from ..ui.screens.victory_screen import VictoryScreen
from ..input.mouse import InputController
from ..game.ai_solver import AiSolver

     
class GameApp:
    def __init__(self):
        pg.display.set_caption("Minesweeper", icontitle="Minesweeper") #Set the window caption to say "Minesweeper"
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.init()
        self.clock = pg.time.Clock()
        self.input = InputController()
        self.state = 'start'
        self.ai = None
        self.player = 'human'
        self.interact = False
        self.difficulty = None
        self.play_screen = None #Will be initialized when transitioning to play state

    def transition_to_play(self, num_mines): #Called by StartScreen when play button is pressed
        self.start_screen = None #Clear the start screen
        self.play_screen = PlayScreen(self.screen, num_mines, self) #Initialize the play screen with the selected number of mines
        self.state = 'play'
        '''
        I found that playing auto-AI mode and transitioning back to human only mode led to the wrong "you lose" message
        being printed.
        '''
        self.player = 'human'

    def transition_to_ai_play(self, num_mines, difficulty):
        self.start_screen = None
        self.play_screen = PlayScreen(self.screen, num_mines, self)
        self.difficulty = difficulty
        self.state = 'ai play'

    def transition_to_game_over(self): #Called by PlayScreen when the game is Over
        self.play_screen = None #Clear the play screen
        self.game_over_screen = GameOverScreen(self.screen, self) #Initialize the game over screen
        self.state = 'game_over'
        print(f"State changed to {self.state}")

    def transition_to_victory(self, elapsed_time): #Called by PlayScreen when the game is won
        self.play_screen = None #Clear the play screen
        self.victory_screen = VictoryScreen(self.screen, self, elapsed_time) #Initialize the victory screen
        self.state = 'victory'

    def transition_to_start(self): #Called by GameOverScreen when restart button is pressed
        self.game_over_screen_screen = None #Clear the play screen
        self.start_screen = StartScreen(self.screen, self) #Re-initialize the start screen
        self.state = 'start'

    def run(self):
        #Main game loop, manages state transitions and screen updates
        running = True
        start_screen = StartScreen(self.screen, self) #We only want to initialize the start screen once, or else it will keep overwriting itself - MJ
                                                    #Pass self to allow StartScreen to call back to GameApp, that becomes the app parameter in StartScreen
        while running:
            #print(self.state)
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    running = False
                else:
                    '''
                    If there's no predicate here, a player can interfere with the AI's moves, even during auto mode. 
                    However, transitions to the game_over state are rely on a timer set in the PlayScreen class, which 
                    can only handle it if the handle() event is called.

                    The self.player=='human' predicate allows human input to actually be handled.

                    The first subpredicate of the second half of the expressions allows human input to be handled if the AI has already lost the game.

                    The second subpredicate ensures that the human can select buttons after the game is over and the PlayScreen has been erased.
                    '''
                    if self.player == 'human' or (self.player == 'ai' and ((self.play_screen and (self.play_screen.loss or self.play_screen.board_cleared))) or not self.play_screen):
                        self.input.handle(e)  # convert to Uncover/ToggleFlag commands
                    pass
            #STATE MANAGEMENT
            if self.state == 'start':
                start_screen.draw()
                self.input.update_screen(start_screen) #Make sure the input controller knows which screen is active
            elif self.state == 'play' and self.play_screen: #Manage Play state
                self.play_screen.draw() #Draw the play screen
                self.input.update_screen(self.play_screen) #Make sure the input controller knows which screen is active

                # You might notice we change the state to 'play' and the player to 'human' in the 'ai play' state during Interactive Mode
                    # Why not reverse that here? Because we have to wait for the 'human' to actually make their move.
                    # Refer to play_screen.py's handle_event method to see where we set the state to 'ai play' and the player to 'ai'

            elif self.state == 'ai play' and self.play_screen:
                if self.ai == None: # When we first start AI mode, we need to create our AI
                    self.ai = AiSolver() # Create the AI
                    self.player = 'ai' # Set the active player to AI
                if self.player == 'ai': 
                    #Show the user what the board looks like before the AI makes its move.
                    self.play_screen.draw()
                    #Give the user time to see it.
                    time.sleep(1)
                    #Let AI make its move.
                    self.ai.AIMove(self.play_screen, self.difficulty) # Make a move when active player is AI
                    
                    '''
                    Deleted, since these steps aren't needed after all. Essentially, the user needs to 
                    be able to see the state of the board BEFORE the AI makes its move. Once the AI makes
                    a move, we don't actually need to wait a second before passing control back to the user.
                    However, when passing control to the AI, we can wait one second.

                    This timing system was put in place so that the timing of the sound effects, particularly for AI
                    moves, would keep up with the screen changes as closely as possible.
                    '''
                    #Show the user the board after AI's move.
                    #self.play_screen.draw()
                    #Give the player a second to view it before its their turn.
                    #time.sleep(1)
                    if self.interact: # If we are in Interactive mode...
                        #print("ITS ME!")
                        self.state = 'play' # ...set the state back to 'play'...
                        self.player = 'human' # ...mark the active player as 'human'     
                
                '''
                I found that I could keep resetting the game during AI auto mode, since the input's screen variable
                was never updated in this step. The for loop above was passing my mouse clicks to the StartScreen and screwing
                everything up.
                '''
                self.input.update_screen(self.play_screen)      
            elif self.state == 'game_over' and self.game_over_screen: #Manage Game Over state
                self.game_over_screen.draw() #Draw the game over screen
                self.ai = None
                self.input.update_screen(self.game_over_screen) #Make sure the input controller knows which screen is active
            elif self.state == 'victory' and self.victory_screen: #Manage Game Over state
                self.victory_screen.draw() #Draw the victory screen
                self.ai = None
                self.input.update_screen(self.victory_screen) #Make sure the input controller knows which screen is active

            #END STATE MANAGEMENT

            pg.display.flip()
            self.clock.tick(FPS)
        pg.quit()
