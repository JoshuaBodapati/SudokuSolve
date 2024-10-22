# Sudoku Solver with Pygame

A graphical Sudoku solver built using Python's `pygame` library. This application allows users to:
- Manually input Sudoku puzzles.
- Solve the puzzles automatically.
- Randomize the board to start a new game.

![sudoku-solver-screenshot](./assets/sudoku-solver-screenshot.png)

## Features
- **Manual Input**: Click on any cell and use the keyboard (1-9) to input numbers.
- **Automatic Solver**: Press `Enter` to solve the current puzzle automatically.
- **Reset Board**: Press `C` to reset the board to its original state.
- **Randomize Board**: Press `R` to generate a randomized starting puzzle.

## Prerequisites
- Python 3.x
- Pygame library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sudoku-solver.git
   cd sudoku-solver
2. Install the required dependencies:
   ```bash
   pip install pygame

## How to Run

1. Run the script
   ```bash
   python sudoku_solver.py

2. The pygame window will open, and you can interact with the following controls
   - **Mouse**: Click on cells to select them
   - **Keyboard**:
     - Press 1-9 to enter a number in the selected cell.
     - Press Backspace to clear a cell.
     - Press Enter to solve the Sudoku puzzle.
     - Press C to reset the board.
     - Press R to randomize the board.
    
## How It Works

- **Automatic Solver**: The solver uses a recursive backtracking algorithm to fill in the puzzle
- **Board Randomization**:     The randomizer adds random valid numbers to the board, following Sudoku rules.

## Future Improvements

- Generate Puzzles with varying difficulty depending on user input.
- Add a user-friendly menu to switch between manual and automatic modes.

## Contact

Created by Joshua Bodapati - feel free to reach out!












   
