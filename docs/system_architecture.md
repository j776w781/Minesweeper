-main.py: entry point for the program. Calls game manager which starts running game logic.

Game Manager:
    Start, call home screen
    Create board
    Track board state (cells, mine placement, flag placement)

UI Screens
    start_screen.py: shows # of mines, has the play button
    ->
    play_screen.py: show UI for board.
    ->
    game_over_screen.py
    ->
    start_screen.py

Models
    board.py: contains backend for the board data and contains cell data
    ->
    cell.py: contains cell class which contains cell properties of uncovered, covered, flags
    