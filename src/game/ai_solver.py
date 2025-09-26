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
        self.firstMove = True
        self.legalMoves = []


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
        self.legalMoves = []
        for i in range(0, 100):
            self.legalMoves.append(i)
        screen.draw()
        if self.firstMove:
            new_event = pg.event.Event(pg.MOUSEBUTTONDOWN, {'button': 1, 'pos': (75, 110)})
            screen.handle_event(new_event)
            self.firstMove = False

        for index in range(len(screen.grid)):
            if screen.grid[index].is_mine:
                bad_index = self.legalMoves.index(index)
                self.legalMoves.pop(bad_index)
            elif not screen.grid[index].is_covered:
                bad_index = self.legalMoves.index(index)
                self.legalMoves.pop(bad_index)

        move = random.choice(self.legalMoves)
        if move > 9:
            move = str(move)
            y = int(move[0])
            x = int(move[1])
        else:
            y = 0
            x = move

        new_event = pg.event.Event(pg.MOUSEBUTTONDOWN, {'button': 1, 'pos': (75 + (40*x), 110 + (40*y))})
        screen.handle_event(new_event)

        if screen.remaining_cells == 0:
            screen.play_state = 'game_over'

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
                screen.draw()
                time.sleep(1)
                screen.end_game()


