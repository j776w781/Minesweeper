"""
Program name: settings.py
Description: Settings and constants for the minesweeper game
Inputs: None
Outputs: Constants
External sources:
Authors: Benjamin Kozlowski
Creation date: 28 August 2025
"""
import pygame

GRID = 10
TILE_PX = 48
MARGIN = 16
HUD_H = 64
WIDTH = MARGIN*2 + GRID*TILE_PX
HEIGHT = MARGIN*2 + GRID*TILE_PX + HUD_H
FPS = 60
#variables used for board.py
BOX_WIDTH = 400
BOX_HIGHT = 400
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
BOX_X = (WIDTH-BOX_WIDTH)//2
BOX_Y = (HEIGHT-BOX_HIGHT)//2
BLOCKSIZE = 40
NUM_COLS = BOX_WIDTH // BLOCKSIZE
NUM_ROWS = BOX_HIGHT // BLOCKSIZE
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))