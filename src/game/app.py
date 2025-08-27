import pygame as pg
from .settings import WIDTH, HEIGHT, FPS
from ..model.game_manager import GameManager
from ..ui.renderer import Renderer
from ..input.controller import InputController

class GameApp:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.manager = GameManager(grid_size=10, mines=10)  # validate 10–20 elsewhere
        self.renderer = Renderer(self.screen, self.manager)
        self.input = InputController(self.manager)

    def run(self):
        running = True
        while running:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    running = False
                else:
                    self.input.handle(e)  # convert to Uncover/ToggleFlag commands

            self.renderer.draw()  # reads manager state only
            pg.display.flip()
            self.clock.tick(FPS)
        pg.quit()
