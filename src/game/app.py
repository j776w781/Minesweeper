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

    def transition_to_ai_play(self, num_mines, difficulty):
        self.start_screen = None
        self.play_screen = PlayScreen(self.screen, num_mines, self)
        self.difficulty = difficulty
        self.state = 'ai play'

    def transition_to_game_over(self): #Called by PlayScreen when the game is Over
        self.play_screen = None #Clear the play screen
        self.game_over_screen = GameOverScreen(self.screen, self) #Initialize the game over screen
        self.state = 'game_over'

    def transition_to_victory(self): #Called by PlayScreen when the game is won
        self.play_screen = None #Clear the play screen
        self.victory_screen = VictoryScreen(self.screen, self) #Initialize the victory screen
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
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    running = False
                else:
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
                    self.ai.AIMove(self.play_screen, self.difficulty) # Make a move when active player is AI
                    if self.interact: # If we are in Interactive mode...
                        self.state = 'play' # ...set the state back to 'play'...
                        self.player = 'human' # ...mark the active player as 'human'           
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
