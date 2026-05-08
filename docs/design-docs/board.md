# Board module

This module implements the `Board` class for the Checkers CLI game.

## Architecture

The `Board` class represents the 8x8 checkers board with:

- **Piece representation**: `"r"`=red man, `"R"`=red king, `"w"`=white man, `"W"`=white king, `"_"`=empty
- **Coordinate system**: (row, col) where row 0-7 (top-to-bottom), col 0-7 (left-to-right)

## Implementation Details

### Initialization

The board is initialized with checkers in standard starting positions:
- Red pieces on rows 0-2 (bottom of visual board)
- White pieces on rows 5-7 (top of visual board)
- Pieces only placed on dark squares (where row+col is odd)

### Move Validation

The `is_valid_move()` method validates moves according to checkers rules:
- Pieces move diagonally forward (red moves down, white moves up)
- Kings move diagonally in both directions
- Single moves: one square diagonally
- Capture moves: two squares diagonally, jumping over opponent piece
- Captured pieces must be removed

### King Promotion

Pieces are promoted to kings when they reach the opposite end:
- Red men become kings when reaching row 7
- White men become kings when reaching row 0

### Winner Detection

The `check_winner()` method returns:
- `"red"` if all white pieces are captured
- `"white"` if all red pieces are captured
- `None` if the game continues

## Usage

```python
from src.board import Board

board = Board()
print(board.display())

# Validate and apply moves
if board.is_valid_move(2, 1, 3, 2, "red"):
    board.apply_move(2, 1, 3, 2)

winner = board.check_winner()
```
