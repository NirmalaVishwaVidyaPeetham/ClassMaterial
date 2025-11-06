# https://github.com/sholker/BrainVita/tree/master 

# BrainVITA Game

## Introduction
This project implements the BrainVITA game using the Pygame library in Python. BrainVITA is a puzzle game played on a board with holes. The goal of the game is to remove all pegs from the board except one, ideally ending with only one peg in the center hole.

## Installation
To run the game, make sure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).
python version 3.9.1 above.

Additionally, you need to install the Pygame library. You can install Pygame using pip, the Python package installer, by running the following command:

`pip install pygame`

## Usage
To start the game, run the `brainvita.py` script using Python:
`python brainvita.py`

Once the game starts, you can interact with it using your mouse. Click on a peg to select it, then click on an adjacent empty hole to move the peg to that position. The game ends when only one peg is left on the board.

## Controls
- Left Mouse Button: Select peg or move peg
- Mouse Click on "Reset": Reset the game board
- Close Button (X): Quit the game

### follow steps
-  . is not included in the board game
-  0 is empty hole
-  1 is a peg

```
. . X X X . . 
. . X X X . . 
X X X X X X X 
X X X X X X X 
X X X 0 X X X 
. . X X X . . 
. . X X X . . 
. . X X X . . 
```

