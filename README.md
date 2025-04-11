# Tic-Tac-Toe Game with AI Opponent

## Overview

A Python implementation of the classic Tic-Tac-Toe game with a graphical interface using Tkinter. Features three difficulty levels for the computer opponent, from random moves to an unbeatable AI using the minimax algorithm.

## Features

- 🎮 **Player vs Computer gameplay**
- 🏆 **Three difficulty levels**:
  - **Easy**: Computer makes random moves
  - **Medium**: Computer blocks wins and takes winning moves
  - **Hard**: Unbeatable AI using minimax algorithm
- ♻️ **Reset game** functionality
- 🏁 **Win/draw detection** with popup notifications
- 🔒 **Input validation** prevents overwriting moves

## Installation

1. Ensure you have Python 3.x installed
2. Clone this repository:
   ```bash
   git clone https://github.com/Dibij/Tic-Tac-Toe.git
   cd Tic-Tac-Toe
   ```
3. Run the game:
   ```bash
   python tictactoe.py
   ```

## How to Play

1. Select your preferred difficulty level
2. Click on any empty square to place your "X"
3. The computer will automatically respond with "O"
4. Try to get three in a row horizontally, vertically, or diagonally
5. Click "Reset Game" to start a new match

## Code Improvements from Original Version

- Added **three difficulty levels** with different AI strategies
- Implemented **minimax algorithm** for unbeatable hard mode
- Fixed **game flow issues** where computer wouldn't respond
- Added **button state management** (DISABLED/NORMAL)
- Improved **win detection** and game over handling
- Enhanced **UI layout** with difficulty selector
- Added **proper input validation** to prevent move overwrites

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## Future Enhancements

- [ ] Score tracking
- [ ] Player vs Player mode
- [ ] Animated moves
- [ ] Sound effects
- [ ] Theme customization

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
