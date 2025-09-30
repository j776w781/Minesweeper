"""
Program name: main
Description: Driver code to create a single entry point for the game
Inputs: None
Outputs: Minesweeper game app
External sources: None
Authors: Will
Creation date: 28 August 2025
"""

from src.game.app import GameApp #GameApp will serve as the core manager of the program

#it is a best practice to keep main simple and just as an entry point for the program
if __name__ == "__main__": #entry point for the program
    GameApp().run() #runs the whole program, calls app which is the manager of the program
