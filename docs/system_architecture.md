Components:
    - main.py: Entry point for the program that calls GameApp to start running game logic.
    - settings.py: Stores values for constants used in the game with descriptive names 
    - GameApp in app.py: Main game loop, controls screen updates and transitions between states (start, play, game over, victory)
    - InputController in mouse.py: Handles mouse clicks (left click to uncover, right click to flag)
    - board.py: Contains cell data in a list, renders cells on the board, renders row and column labels
    - Cell in cell.py: Contains properties of a single cell (is mine, is covered, is flagged, number of adjacent mines) and has methods to change properties and render the cell
    - StartScreen in start_screen.py: UI for the start screen when the game launches, displays number of mines with buttons to increase or decrease mine count, gives option to start game
    - PlayScreen in play_screen.py: Game UI, renders the grid, game state (Ready, Playing, You Lose!, You Win!), and remaining mine count, and handles game events
    - GameOverScreen in game_over_screen.py: UI for the game over screen when the player loses, gives option to restart
    - VictoryScreen in victory_screen.py: UI for the victory screen when the player wins, gives option to restart
    - Button in button.py: Renders a button with text and action

Data Flow:
    - User input (click) -> InputController validates and sends to the active screen's event handler

Key Data Structures:
    -

Assumptions:
    - Fixed 10x10 grid size
    - Mine count user-specified (10-20) at game start