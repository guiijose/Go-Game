# Go Game

This is a Python implementation of the **Go** board game, a classic strategy game where two players compete to capture territory on a grid board. The project simulates the rules, gameplay, and strategies involved in Go.

## Features
- Supports local two-player gameplay.
- Implements Go rules, including stone capture and territory control.
- Allows players to place stones on a board, with turn-based interaction.
- Handles scoring based on areas controlled and captured stones.
- Terminal based interface.

## Tests

The project's tests are located in the `public/` folder. To run the tests, use the following command:

```bash
python -m unittest discover -s public 
```
## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/go-game.git
   ```
2. Edit the code and call the function ```go(tamanho, ib, ip)``` where **tamanho** is the size of the board (9, 13, or 19) and **ib** and **ip** are the lists with the positions of the whites and blacks, respectively.
3. Then run the following command:
   ```
   python main.py
   ```
4. Or if in Mac or Linux use:
   ```
   python3 main.py
   ```
   
