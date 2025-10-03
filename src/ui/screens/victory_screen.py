"""
Program name: victory_screen
Description: displays the victory screen of minesweeper
Inputs: takes in the app state and the screen
Outputs: ui for the Victory screen with restart button
External sources: None
Authors: Will
Creation date: 7 September 2025
"""


import pygame as pg
from ..button import Button
import json
import os


class VictoryScreen:
    def __init__(self, screen, app=None, elapsed_time=None): 
        #Initialize the start screen
        #It has app paramater so that it an communicate back to the main GameApp to trigger state changes.
        self.screen = screen
        self.app = app
        self.font = pg.font.Font(None, 74)
        self.small_font = pg.font.Font(None, 36)
        self.interactibles = list()
        self.elapsed_time = elapsed_time

        # Load record time from file
        self.record_path = "record.json"
        self.record_time = self.load_record_time()

        self.restart_button = Button(
            x=screen.get_width() // 2 - 100,
            y=screen.get_height() // 2,
            width=200,
            height=50,
            text="Restart",
            action=self.restart_game
        )
        self.interactibles.append(self.restart_button)

    def load_record_time(self):
        """Load the record time from JSON file if it exists."""
        if os.path.exists(self.record_path):
            try:
                with open(self.record_path, "r") as f:
                    data = json.load(f)
                    return data.get("record_time", None)
            except Exception:
                return None
        return None

    def save_record_time(self):
        """Save the record time to JSON file."""
        try:
            with open(self.record_path, "w") as f:
                json.dump({"record_time": self.record_time}, f)
        except Exception as e:
            print("Error saving record time:", e)
    #Start the game when restart button is pressed
    #Calls back to the main GameApp to transition to restart state
    #defined only if app is provided
    def restart_game(self):
        if hasattr(self, 'app') and self.app: #Check to make sure app exists as a good practice
            self.app.transition_to_start() #Call the transition_to_start method in GameApp

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear screen with black

        #Title
        title_surface = self.font.render("Victory", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(self.screen.get_width() // 2, 100))
        self.screen.blit(title_surface, title_rect)

        #Timer display

        if self.elapsed_time is not None:
            minutes = int(self.elapsed_time // 60)
            seconds = int(self.elapsed_time % 60)
            formatted_time = f"{minutes}:{seconds:02d}"  # pad seconds with 0 if needed
        else:
            formatted_time = "0:00"

        timer_surface = self.small_font.render(f"Time: {formatted_time}", True, (255, 255, 255))
        timer_surface = self.small_font.render("Time: {}".format(formatted_time), True, (255, 255, 255))
        timer_rect = timer_surface.get_rect(center=(self.screen.get_width() // 2, 200))
        self.screen.blit(timer_surface, timer_rect)

        # Record fastest time taken to win
        if (self.record_time == None):
            self.record_time = self.elapsed_time
            self.save_record_time()
        elif (self.elapsed_time < self.record_time):
            self.record_time = self.elapsed_time
            self.save_record_time()

        #Record Timer display
        if self.record_time is not None:
            minutes = int(self.record_time // 60)
            seconds = int(self.record_time % 60)
            formatted_time = f"{minutes}:{seconds:02d}"  # pad seconds with 0 if needed
        else:
            formatted_time = "0:00"

        #Create the record time surface
        record_surface = self.small_font.render(f"Record Time: {formatted_time}", True, (255, 255, 255))
        record_surface = self.small_font.render("Record Time: {}".format(formatted_time), True, (255, 255, 255))
        record_rect = record_surface.get_rect(center=(self.screen.get_width() // 2, 250))
        self.screen.blit(record_surface, record_rect)

        #Draw restart button
        self.restart_button.draw(self.screen)

    #When an event is called
    def handle_event(self, event):
        for button in self.interactibles: #Check to see which interactible it hit
            button.handle_event(event)