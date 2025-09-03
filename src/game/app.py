"""
Program name:
Description:
Inputs:
Outputs:
External sources:
Authors:
Creation date: 28 August 2025
"""

import pygame as pg
from .settings import WIDTH, HEIGHT, FPS
from ..ui.screens.start_screen import StartScreen
from ..ui.screens.play_screen import PlayScreen
from ..input.mouse import InputController
     
class GameApp:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.input = InputController()
        self.state = 'start'
        self.play_screen = None #Will be initialized when transitioning to play state

    def transition_to_play(self, num_mines): #Called by StartScreen when play button is pressed
        self.play_screen = PlayScreen(self.screen, num_mines) #Initialize the play screen with the selected number of mines
        self.state = 'play'

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
            #END STATE MANAGEMENT

            pg.display.flip()
            self.clock.tick(FPS)
        pg.quit()
