# Game Module Design

## Overview

The `game.py` module implements the `Game` class that manages the overall game state for the Checkers CLI game. It handles turn management, win detection, and move execution.

## Architecture

```
Game
├── _board: Board
├── _current_player: str
├── current_player (property)
├── is_game_over()
├── get_valid_moves(player)
├── execute_move(from_row, from_col, to_row, to_col)
└── switch_turn()
```

## Implementation Details

### Turn Management

The game alternates between "red" and "white" players. The `_current_player` attribute tracks whose turn it is. The `switch_turn()` method toggles between players after each successful move.

### Win Detection

The game ends when:
1. One player has no pieces on the board (detected by `Board.check_winner()`)
2. The current player has no valid moves (checked by `get_valid_moves()`)

The `is_game_over()` method returns `True` if either condition is met.

### Move Execution

`execute_move()` validates a move against the board, applies it if valid, and switches turns. Returns `True` for valid moves, `False` otherwise.

### Valid Moves

`get_valid_moves(player)` scans the entire board to find all legal moves for a given player. It:
1. Iterates through all board positions
2. Filters pieces by player color
3. Tests each potential destination with `Board.is_valid_move()`
4. Returns a list of (from_row, from_col, to_row, to_col) tuples

## Dependencies

- `Board` class from `src.board` - provides piece state, move validation, and capture detection

## Non-Obvious Constraints

1. The board module must implement the exact interface specified in `ARCHITECTURE.md` for `Game` to work correctly
2. Move notation uses (row, col) coordinates where row 0-7 is top-to-bottom and col 0-7 is left-to-right
3. Player names are "red" and "white" (not "red player" or other variants)
4. The game checks for valid moves on the current player's turn - if they have none, the game ends even if the opponent could still play
