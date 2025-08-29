#has number of mines and play button
import pygame as pg
from ..button import Button

class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pg.font.Font(None, 74)
        self.small_font = pg.font.Font(None, 36)
        self.num_mines = 10  # Default number of mines

        self.play_button = Button(
            x=screen.get_width() // 2 - 100,
            y=screen.get_height() // 2,
            width=200,
            height=50,
            text="Play",
            action=self.start_game
        )

    def start_game(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear screen with black

        title_surface = self.font.render("Minesweeper", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(self.screen.get_width() // 2, 100))
        self.screen.blit(title_surface, title_rect)

        mines_surface = self.small_font.render(f"Number of Mines: {self.num_mines}", True, (255, 255, 255))
        mines_rect = mines_surface.get_rect(center=(self.screen.get_width() // 2, 200))
        self.screen.blit(mines_surface, mines_rect)

        self.play_button.draw(self.screen)

    def handle_event(self, event):
        self.play_button.handle_event(event)