"""
Program name: start_screen
Description: prints the start screen ui with a start button and takes input of number of mines 
Inputs: takes in number of mines
Outputs: start screen ui with mine number buttons
External sources: PyGame Documentation
Authors: Will
Creation date: 28 August 2025
"""

#has number of mines and play button
import pygame as pg
from ..button import Button

class StartScreen:
    def __init__(self, screen, app=None): 
        #Initialize the start screen
        #It has app paramater so that it an communicate back to the main GameApp to trigger state changes.
        self.screen = screen
        self.app = app
        self.font = pg.font.Font(None, 74)
        self.small_font = pg.font.Font(None, 36)
        self.num_mines = 10  # Default number of mines
        self.interactibles = list()

        self.play_button = Button(
            x=screen.get_width() // 2 - 100,
            y=screen.get_height() // 2,
            width=200,
            height=50,
            text="Play",
            action=self.start_game
        )
        self.interactibles.append(self.play_button)

        # Auto mode button
        self.auto_button = Button(
            x=screen.get_width() // 2 - 80,
            y=screen.get_height() // 2 + 200,
            width=100,
            height=50,
            text="Auto",
            action=self.toggle_auto
        )
        self.interactibles.append(self.auto_button)

        #Interactive mode button
        self.inter_button = Button(
            x=screen.get_width() // 2 + 30,
            y=screen.get_height() // 2 + 200,
            width=140,
            height=50,
            text="Interactive",
            action=self.toggle_interact
        )
        self.interactibles.append(self.inter_button)

        #Increase mines button
        self.increment_button = Button(
            x=screen.get_width() // 2 + 130,
            y=screen.get_height() // 2 - 120,
            width=30,
            height=30,
            text="+1",
            action=self.more_mines
        )
        self.interactibles.append(self.increment_button)

        #Decrease mines button
        self.decrement_button = Button(
            x=screen.get_width() // 2 + 130,
            y=screen.get_height() // 2 - 80,
            width=30,
            height=30,
            text="-1",
            action=self.less_mines
        )
        self.interactibles.append(self.decrement_button)


        self.easy_button = Button(
            x=screen.get_width() // 2 - 80,
            y=screen.get_height() // 2 + 100,
            width=100,
            height=50,
            text="Easy",
            action=self.enable_easy_ai
        )
        self.interactibles.append(self.easy_button)

        self.med_button = Button(
            x=screen.get_width() // 2 +30,
            y=screen.get_height() // 2 + 100,
            width=100,
            height=50,
            text="Medium",
            action=self.enable_medium_ai
        )
        self.interactibles.append(self.med_button)

        self.hard_button = Button(
            x=screen.get_width() // 2 +140,
            y=screen.get_height() // 2 + 100,
            width=100,
            height=50,
            text="Hard",
            action=self.enable_hard_ai
        )
        self.interactibles.append(self.hard_button)

    #Start the game when play button is pressed
    #Calls back to the main GameApp to transition to play state
    #defined only if app is provided
    def start_game(self):
        if hasattr(self, 'app') and self.app: #Check to make sure app exists as a good practice
            self.app.transition_to_play(self.num_mines) #Call the transition_to_play method in GameApp with the selected number of mines

    #Go into AI mode...whatever that means...
    def enable_easy_ai(self):
        if hasattr(self, 'app') and self.app:
            self.app.transition_to_ai_play(self.num_mines, 'easy')

    def enable_medium_ai(self):
        if hasattr(self, 'app') and self.app:
            self.app.transition_to_ai_play(self.num_mines, 'medium')

    def enable_hard_ai(self):
        if hasattr(self, 'app') and self.app:
            self.app.transition_to_ai_play(self.num_mines, 'hard')

    def toggle_interact(self):
        self.app.auto = False
        self.app.interact = True
    
    def toggle_auto(self):
        self.app.interact = False
        self.app.auto = True

    #Increase the amount of mines 
    def more_mines(self):
        if self.num_mines != 20: #If the number of mines is not 20
            #print("adding a mine")
            self.num_mines += 1 #Add 1

    #Decrease the amount of mines
    def less_mines(self):
        if self.num_mines != 10: #If the number of mines is not 10
            self.num_mines -= 1 #Subtract 1

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear screen with black

        #Title
        title_surface = self.font.render("Minesweeper", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(self.screen.get_width() // 2, 100))
        self.screen.blit(title_surface, title_rect)

        #Number of mines
        mines_surface = self.small_font.render(f"Number of Mines: {self.num_mines}", True, (255, 255, 255))
        mines_rect = mines_surface.get_rect(center=(self.screen.get_width() // 2, 200))
        self.screen.blit(mines_surface, mines_rect)

        #Draw increment button
        self.increment_button.draw(self.screen)

        #Draw decrement button
        self.decrement_button.draw(self.screen)

        #Draw play button
        self.play_button.draw(self.screen)


        #Number of mines
        ai_diff_surface = self.small_font.render("AI Difficulty: ", True, (255, 255, 255))
        ai_diff_rect = ai_diff_surface.get_rect(center=(self.screen.get_width() // 6, 400))
        self.screen.blit(ai_diff_surface, ai_diff_rect)


        #Draw ai button
        self.auto_button.draw(self.screen)

        self.inter_button.draw(self.screen)

        self.easy_button.draw(self.screen)

        self.med_button.draw(self.screen)

        self.hard_button.draw(self.screen)

    #When an event is called
    def handle_event(self, event):
        for button in self.interactibles: #Check to see which interactible it hit
            button.handle_event(event)