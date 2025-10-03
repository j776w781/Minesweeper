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
from operator import itemgetter


class LeaderBoardScreen:
    def __init__(self, screen, app=None, leaderboard = None): 
        #Initialize the start screen
        #It has app paramater so that it an communicate back to the main GameApp to trigger state changes.
        self.screen = screen
        self.app = app
        self.font = pg.font.Font(None, 74)
        self.small_font = pg.font.Font(None, 36)
        self.interactibles = list()
        self.leaderboard = leaderboard

        self.back_button = Button(
            x=screen.get_width() // 2 - 100,
            y=screen.get_height() // 2+200,
            width=200,
            height=50,
            text="Back",
            action=self.back_to_start
        )
        self.interactibles.append(self.back_button)

    def display_leaderboard(self, screen, start_x, start_y, max_entries=10):        
        
        sorted_lb = sorted(self.leaderboard,reverse=False)#sort data
        
        # 2. Render Title
        title_surface = self.font.render("Leaderboard", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(screen.get_width() // 2, start_y))
        screen.blit(title_surface, title_rect)
        
        # Starting position for the list entries
        y_offset = title_rect.height + 20 
        

        # 3. Render Entries
        for rank, entry in enumerate(sorted_lb[:max_entries]):
            time = entry
            minutes = int(time) // 60
            seconds = int(time) % 60
            formatted_time = f"{minutes}:{seconds:02d}"
            text = formatted_time
            text_surface = self.font.render(text, True, (255,255,255))
            x = start_x
            y = start_y + y_offset + (rank * (50 + 5)) # Add spacing
            
            # Blit the text
            screen.blit(text_surface, (x, y))


    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear screen with black

        self.display_leaderboard(self.screen,(self.screen.get_width()-125) // 2, 50, max_entries=5)

        self.back_button.draw(self.screen)

    def back_to_start(self):
        if hasattr(self, 'app') and self.app: #Check to make sure app exists as a good practice
            self.app.transition_to_start() #Call the transition_to_start method in GameApp

    #When an event is called
    def handle_event(self, event):
        for button in self.interactibles: #Check to see which interactible it hit
            button.handle_event(event)