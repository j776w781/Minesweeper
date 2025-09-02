import pygame as pg
from .settings import WIDTH, HEIGHT, FPS
from ..ui.screens.start_screen import StartScreen
from ..input.mouse import InputController
     
class GameApp:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.input = InputController()
        self.state = 'start'


    def run(self):
        running = True
        start_screen = StartScreen(self.screen) #We only want to initialize the start screen once,
                                                #or else it will keep overwriting itself - MJ
        while running:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    running = False
                else:
                    self.input.handle(e)  # convert to Uncover/ToggleFlag commands
                    pass
            if self.state == 'start':
                start_screen.draw()
                self.input.update_screen(start_screen) #Make sure the input controller knows which screen is active


            pg.display.flip()
            self.clock.tick(FPS)
        pg.quit()
