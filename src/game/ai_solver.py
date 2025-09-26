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
        pass


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
        screen.draw()
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        new_event = pg.event.Event(pg.MOUSEBUTTONDOWN, {'button': 1, 'pos': (75 + (40*x), 110 + (40*y))})
        screen.handle_event(new_event)
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
                screen.end_game()

    def mediumMode(self, screen):
        print("Medium mode enabled")

    def hardMode(self, screen):
        print("Hard mode enabled")

