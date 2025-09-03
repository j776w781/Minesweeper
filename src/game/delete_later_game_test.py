import pygame as pg

# Set variables
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
running = True
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
BOX_X = 100
BOX_Y = 100
BOX_WIDTH = 400
BOX_HIGHT = 400
BLOCKSIZE = 20
NUM_COLS = BOX_WIDTH // BLOCKSIZE
NUM_ROWS = BOX_HIGHT // BLOCKSIZE


#make display window
pg.init() #start pygame
SCREEN = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #display screen
pg.display.set_caption("Minesweeper Game") #Set the window title

#functions for the game
def make_grid():
    pg.draw.rect(SCREEN, BLACK, (BOX_X, BOX_Y, BOX_WIDTH, BOX_HIGHT), 2)
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            #calculate posistion of cell to box
            cell_x = BOX_X + (col * BLOCKSIZE)
            cell_y = BOX_Y + (row * BLOCKSIZE)

            rect = pg.Rect(cell_x, cell_y, BLOCKSIZE, BLOCKSIZE)
            pg.draw.rect(SCREEN, GRAY, rect, 1)

class PlayScreen:
    def __init__(self, screen, num_mines):
        self.screen = screen
        self.num_mines = num_mines
        self.font = pg.font.Font(None, 74)
        self.small_font = pg.font.Font(None, 36)
        self.grid = make_grid()

    def draw(self):
        self.screen.fill(WHITE)
        make_grid()

        mines_surface = self.small_font.render(f"Mines: {self.num_mines}", True, (BLACK))
        self.screen.blit(mines_surface, (525, 100))

        pg.display.update()


    def handle_event(self, event):
        #for when cells are clicked
        pass

#run the game
play_screen = PlayScreen(SCREEN, 10)
while running:
    SCREEN.fill(WHITE)
    # Event handling
    for event in pg.event.get():
        if event.type == pg.QUIT:  # Check if the user clicked the close button
            running = False

    play_screen.draw()
    pg.display.update()
# Quit Pygame
pg.quit()