import pygame

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
pygame.init() #start pygame
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #display screen
pygame.display.set_caption("Minesweeper Game") #Set the window title

#functions for the game
def MakeGrid():
    pygame.draw.rect(SCREEN, BLACK, (BOX_X, BOX_Y, BOX_WIDTH, BOX_HIGHT), 2)
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            #calculate posistion of cell to box
            cell_x = BOX_X + (col * BLOCKSIZE)
            cell_y = BOX_Y + (row * BLOCKSIZE)

            rect = pygame.Rect(cell_x, cell_y, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(SCREEN, GRAY, rect, 1)

#run the game
while running:
    SCREEN.fill(WHITE)
    MakeGrid()
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if the user clicked the close button
            running = False
    pygame.display.update()
# Quit Pygame
pygame.quit()