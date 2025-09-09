Components:
    - main.py: Entry point for the program that calls GameApp to start running game logic.
    - settings.py: Stores values for constants used in the game with descriptive names 
    - GameApp in app.py: Main game loop, controls screen updates and transitions between states (start, play, game over, victory)
    - InputController in mouse.py:
    - board.py: [contains backend for the board data and contains cell data]
    - Cell in cell.py: [contains cell class which contains cell properties of uncovered, covered, flags]
    - StartScreen in start_screen.py:
    - PlayScreen in play_screen.py:
    - GameOverScreen in game_over_screen.py:
    - VictoryScreen in victory_screen.py:
    - Button in button.py:

Data Flow:
    - User input (click) -> InputController validates and sends to the active screen's event handler

Key Data Structures:
    -

Assumptions:
    - Fixed 10x10 grid size
    - Mine count user-specified (10-20) at game start