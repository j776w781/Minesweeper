"""
Program name:
Description:
Inputs:
Outputs:
External sources:
Authors:
Creation date: 28 August 2025
"""

#Class that defines and handles mouse input

#Import libraries
import pygame as pg

class InputController:
    def __init__(self):
        self.screen = None

    #Handle input events from the app
    def handle(self, event: pg.event.Event):
        if not self.screen == None: #If there is a screen active,
            self.screen.handle_event(event) #Pass it the event
        """
        if event.type == pg.MOUSEBUTTONDOWN: #If the event was a mouse click
            if event.button == 1: #If it was a left click
                print(f"Left click at {event.pos}")
                """
        
    def update_screen(self, screen): #Update the active screen to the given screen
        self.screen = screen