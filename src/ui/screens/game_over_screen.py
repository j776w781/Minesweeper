"""
Program name: Game Over Screen
Description: displays the game over screen of minesweeper
Inputs:
Outputs:
External sources: None
Authors: Will
Creation date: 4 September 2025
"""


import pygame as pg
from ..button import Button

class GameOverScreen:
    def __init__(self, screen, app=None): 
        #Initialize the start screen
        #It has app paramater so that it an communicate back to the main GameApp to trigger state changes.
        self.screen = screen
        self.app = app
        self.font = pg.font.Font(None, 74)
        self.small_font = pg.font.Font(None, 36)
        self.interactibles = list()

        self.restart_button = Button(
            x=screen.get_width() // 2 - 100,
            y=screen.get_height() // 2,
            width=200,
            height=50,
            text="Restart",
            action=self.restart_game
        )
        self.interactibles.append(self.restart_button)


    #Start the game when restart button is pressed
    #Calls back to the main GameApp to transition to restart state
    #defined only if app is provided
    def restart_game(self):
        if hasattr(self, 'app') and self.app: #Check to make sure app exists as a good practice
            self.app.transition_to_start() #Call the transition_to_start method in GameApp

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear screen with black

        #Title
        title_surface = self.font.render("Game Over", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(self.screen.get_width() // 2, 100))
        self.screen.blit(title_surface, title_rect)


        #Draw restart button
        self.restart_button.draw(self.screen)

    #When an event is called
    def handle_event(self, event):
        for button in self.interactibles: #Check to see which interactible it hit
            button.handle_event(event)