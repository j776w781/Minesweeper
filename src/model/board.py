"""
Program name: board.py
Description: Outputs a grid of Cell objects for the minesweeper game
Inputs: none
Outputs: A centered grid of Cell objects with row and column labels
External sources:
Authors: Ruth Higgason, Benjamin Kozlowski
Creation date: 28 August 2025
"""

#imports
import pygame
from ..game.settings import SCREEN, BLACK, BOX_X, BOX_Y, BOX_WIDTH, BOX_HIGHT, NUM_ROWS, NUM_COLS, BLOCKSIZE
from .cell import Cell

#draw grid
def make_grid():
    pygame.draw.rect(SCREEN, BLACK, (BOX_X, BOX_Y, BOX_WIDTH, BOX_HIGHT), 2)
    cell_list = [] #make list to keep cells for the board
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            #calculate posistion of cell to box
            cell_x = BOX_X + (col * BLOCKSIZE)
            cell_y = BOX_Y + (row * BLOCKSIZE)
            cell = Cell() #create cell
            cell.draw(SCREEN, cell_x, cell_y, BLOCKSIZE) #draw cell
            cell_list.append(cell) #add cell to list
    return cell_list #return the list of cells

#add label to the rows and cols of the grid
def make_labels():
    FONT = pygame.font.SysFont('Arial', 24)
    # column labels (top)
    for col in range(NUM_COLS):
        label = FONT.render(chr(col + 65), True, BLACK) #make label
        label_rect = label.get_rect(center=(BOX_X + col*BLOCKSIZE + BLOCKSIZE//2, BOX_Y - 10))
        SCREEN.blit(label, label_rect) #add label to screen
    # row labels (left)
    for row in range(NUM_ROWS):
        label = FONT.render(str(row + 1), True, BLACK) #make label
        label_rect = label.get_rect(center=(BOX_X - 15, BOX_Y + row*BLOCKSIZE + BLOCKSIZE//2))
        SCREEN.blit(label, label_rect) #add label to screen

    