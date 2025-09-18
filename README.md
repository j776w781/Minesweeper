# Minesweeper

A classic Minesweeper game implementation in Python using Pygame. This project was developed as Project 1 for Software Engineering II.

to run the app, in the root folder run command:
python main.py

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Rules](#game-rules)
- [Project Structure](#project-structure)
- [Development](#development)
- [Authors](#authors)

## Overview

This Minesweeper implementation features a 10x10 grid with user-configurable mine counts (10-20 mines). The game includes multiple screens for start menu, gameplay, victory, and game over states, all built with a clean object-oriented architecture.

## Features

- **Classic Minesweeper Gameplay**: Uncover cells, flag mines, and avoid explosions
- **Customizable Difficulty**: Choose between 10-20 mines for varying difficulty levels
- **Intuitive Controls**: Left-click to uncover cells, right-click to flag/unflag
- **Smart First Click**: The first clicked cell and adjacent cells are guaranteed to be mine-free
- **Auto-reveal**: Cells with zero adjacent mines automatically reveal surrounding cells
- **Visual Feedback**: Clear indicators for covered, flagged, and numbered cells
- **Game State Management**: Distinct screens for start, play, victory, and game over
- **Mine Counter**: Real-time display of remaining mines and flags

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd Minesweeper
   ```

2. Install Pygame:
   ```bash
   pip install pygame
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## How to Play

1. **Starting the Game**: Launch the application and select the number of mines (10-20) using the + and - buttons
2. **Click "Play"** to start the game
3. **Left-click** on any cell to uncover it
4. **Right-click** on covered cells to place or remove flags
5. **Win** by uncovering all non-mine cells
6. **Lose** by clicking on a mine

## Game Rules

### Board Setup
- 10x10 grid with columns labeled A-J and rows numbered 1-10
- User-specified number of mines (10-20)
- Mines are randomly placed at game start
- First clicked cell and adjacent cells are guaranteed mine-free

### Gameplay Mechanics
- **Uncovering Cells**: Reveals numbers indicating adjacent mines (0-8)
- **Zero-Adjacent Cells**: Automatically uncover surrounding cells
- **Flagging**: Mark suspected mines with flags
- **Protection**: Flagged cells cannot be uncovered until unflagged
- **Mine Counter**: Shows remaining mines (total mines - placed flags)

### Win/Loss Conditions
- **Victory**: Uncover all non-mine cells without hitting a mine
- **Loss**: Uncover a cell containing a mine


### Core Components

- **GameApp** (`src/game/app.py`): Main application controller managing game states and screen transitions
- **InputController** (`src/input/mouse.py`): Handles mouse input validation and routing
- **Board** (`src/model/board.py`): Manages the game grid, cell data, and board rendering
- **Cell** (`src/model/cell.py`): Represents individual cells with mine, flag, and adjacency properties

### User Interface

- **StartScreen**: Mine count selection and game initialization
- **PlayScreen**: Main game interface with grid, status, and mine counter
- **GameOverScreen**: Loss state with restart option
- **VictoryScreen**: Win state with restart option
- **Button**: Reusable button component for user interactions

### Data Flow

1. User input → InputController validates and routes to active screen
2. Screen event handlers → Update game state (Board/Cell objects)
3. GameApp → Manages state transitions and screen updates
4. UI Components → Render current game state

## Development

### Key Design Decisions

- **State Management**: Centralized in GameApp with clear state transitions
- **Input Handling**: Separated input validation from game logic
- **Modular UI**: Screen-based architecture for easy maintenance
- **Data Structure**: 100-element list representing 10x10 grid using Cell objects


### Documentation

Comprehensive documentation is available in the `docs/` folder:
- System architecture and design decisions
- Detailed requirements specification
- UML diagrams and game flow charts
- Development time tracking and methodology

## Authors

- **Will**
- **MJ**
- **Ben**
- **Eric**
- **Ruth**
**Group 5** - Software Engineering Course

**Creation Date**: August 28, 2025
