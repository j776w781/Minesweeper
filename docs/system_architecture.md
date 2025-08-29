-main.py: entry point for the program. Calls GameApp from app.py which starts running game logic. This will call the start_screen.py.


UI Screens
    start_screen.py: shows # of mines, has the play button
    ->
    play_screen.py: show UI for board.
    ->
    game_over_screen.py
    ->
    start_screen.py
Game Manager:
    Create board
    Track board state (cells, mine placement, flag placement)

Models
    board.py: contains backend for the board data and contains cell data
    ->
    cell.py: contains cell class which contains cell properties of uncovered, covered, flags

Input
    mouse input for the board clicks.