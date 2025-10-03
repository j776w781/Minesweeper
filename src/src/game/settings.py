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
HUD_H = 64
MARGIN = 16
WIDTH = MARGIN*2 + GRID*TILE_PX
HEIGHT = MARGIN*2 + GRID*TILE_PX + HUD_H
FPS = 60
BOX_WIDTH = 400
BOX_HIGHT = 400
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)
BOX_X = (WIDTH-BOX_WIDTH)//2
BOX_Y = (HEIGHT-BOX_HIGHT)//2
BLOCKSIZE = 40
NUM_COLS = BOX_WIDTH // BLOCKSIZE
NUM_ROWS = BOX_HIGHT // BLOCKSIZE
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.init()
pygame.mixer.init()

SOUND_ON = True

#sound assets
CLICK_SOUND = pygame.mixer.Sound("click.mp3")
FLAG_SOUND = pygame.mixer.Sound("flag.mp3")
BOMB_SOUND = pygame.mixer.Sound("bomb.mp3")
