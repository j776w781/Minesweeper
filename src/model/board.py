"""
Program name: board.py
Description: Outputs a grid of Cell objects for the minesweeper game
Inputs: none
Outputs: A centered grid of Cell objects with row and column labels
External sources:
Authors: Ruth Higgason, Benjamin Kozlowski
Creation date: 28 August 2025
"""

import pygame
from ..game.settings import WIDTH, HEIGHT, SCREEN, BLACK, BOX_X, BOX_Y, BOX_WIDTH, BOX_HIGHT, NUM_ROWS, NUM_COLS, BLOCKSIZE, GRAY
from .cell import Cell

#draw grid and add labels
def make_grid():
    FONT = pygame.font.SysFont('Arial', 24)
    pygame.draw.rect(SCREEN, BLACK, (BOX_X, BOX_Y, BOX_WIDTH, BOX_HIGHT), 2)
    cell_list = []
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            #calculate posistion of cell to box
            cell_x = BOX_X + (col * BLOCKSIZE)
            cell_y = BOX_Y + (row * BLOCKSIZE)
            cell = Cell()
            cell.draw(SCREEN, cell_x, cell_y, BLOCKSIZE)
            cell_list.append(cell)


    # column labels (top)
    for col in range(NUM_COLS):
        label = FONT.render(chr(col + 65), True, BLACK)
        label_rect = label.get_rect(center=(BOX_X + col*BLOCKSIZE + BLOCKSIZE//2, BOX_Y - 10))
        SCREEN.blit(label, label_rect)
    # row labels (left)
    
    for row in range(NUM_ROWS):
        label = FONT.render(str(row + 1), True, BLACK)
        label_rect = label.get_rect(center=(BOX_X - 15, BOX_Y + row*BLOCKSIZE + BLOCKSIZE//2))
        SCREEN.blit(label, label_rect)

    return cell_list