import pygame as pg
from .settings import WIDTH, HEIGHT, FPS
from ..ui.screens.start_screen import StartScreen
#from ..input.mouse import InputController

class GameApp:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        #self.input = InputController(self.manager)
        #MJ, add the Input Controller to get the button to work
        self.state = 'start'

    def run(self):
        running = True
        while running:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    running = False
                else:
                   #self.input.handle(e)  # convert to Uncover/ToggleFlag commands
                   #MJ, add the Input Controller to get the button to work
                    pass
            if self.state == 'start':
                start_screen = StartScreen(self.screen)
                start_screen.draw()


            pg.display.flip()
            self.clock.tick(FPS)
        pg.quit()
