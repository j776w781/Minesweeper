# Minesweeper Project Requirements

## Game Setup
- Board Configuration
    - Size: 10x10 grid
    - Columns labeled A–J; rows numbered 1–10
- Mine Configuration
    - Number of mines: User-specified, 10 to 20
    - Randomly placed at game start
    - First clicked cell (and optionally adjacent cells) guaranteed mine-free
    - Initial State: All cells start covered, with no flags

## Gameplay
- Players uncover a cell by selecting it (e.g., clicking)
- Uncovering a mine ends the game (loss)
- Uncovering a mine-free cell reveals a number (0–8) indicating adjacent mines
- Cells with zero adjacent mines trigger recursive uncovering of adjacent cells
- Players can toggle flags on covered cells to mark suspected mines

## Mine Flagging
- Players place/remove flags on covered cells to indicate potential mines
- Flagged cells cannot be uncovered until unflagged
- Display remaining flag count (total mines minus placed flags)

## Player Interface
- Display a 10x10 grid showing cell states: covered, flagged, or uncovered (number or empty for zero adjacent mines)
- Show remaining mine count (total mines minus flags)
- Provide a status indicator (e.g., “Playing,” “Game Over: Loss,” “Victory”)

## Game Conclusion
- Loss: Triggered by uncovering a mine, revealing all mines
- Win: Achieved by uncovering all non-mine cells without detonating any mines