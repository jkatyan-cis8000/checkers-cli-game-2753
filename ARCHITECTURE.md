# ARCHITECTURE.md

Written by team-lead before spawning teammates. This is the shared blueprint —
teammates read it to understand what they are building and how their module fits.
Update it when the structure changes; do not let it drift from the actual code.

## Module Structure

- src/board.py: 8x8 board state, piece representation, move validation, capture detection, king promotion
- src/game.py: turn management, player state, game loop, win detection
- src/ui.py: terminal rendering, move input parsing (e.g., "e6f5"), move notation conversion
- src/main.py: entry point, orchestrates game setup and main loop

## Interfaces

### board.py
- `Board`: class representing the 8x8 grid
  - `__init__(): None` - initialize empty board with starting positions
  - `display(): str` - return string representation of board
  - `get_piece(row, col): str | None` - get piece at position (row, col)
  - `is_valid_square(row, col): bool` - check if coordinates are on board
  - `is_valid_move(from_row, from_col, to_row, to_col, player): bool` - validate move
  - `apply_move(from_row, from_col, to_row, to_col): None` - execute move including captures
  - `is_king(row, col): bool` - check if piece is a king
  - `make_king(row, col): None` - promote piece to king
  - `check_winner(): str | None` - return "red", "white", or None if game continues

### game.py
- `Game`: class managing game state
  - `__init__(): None` - initialize game with board and players
  - `current_player: str` - property returning current player ("red" or "white")
  - `is_game_over(): bool` - check if game has ended
  - `get_valid_moves(player): list[tuple]` - get all valid moves for player
  - `execute_move(from_row, from_col, to_row, to_col): bool` - validate and execute move
  - `switch_turn(): None` - switch to next player

### ui.py
- `UI`: class handling user interaction
  - `parse_move(move_str: str) -> tuple[int, int, int, int]` - parse "e6f5" to (from_row, from_col, to_row, to_col)
  - `display_board(board): None` - print board to terminal
  - `get_player_input(player: str) -> str` - prompt player for move
  - `display_message(msg: str): None` - print message to terminal
  - `display_winner(winner: str): None` - announce game winner

### main.py
- `main(): None` - entry point, runs game loop until completion

## Shared Data Structures

- Position notation: alphanumeric like "e6" where column a-h (left-to-right), row 1-8 (bottom-to-top)
- Internal coordinates: (row, col) where row 0-7 (top-to-bottom), col 0-7 (left-to-right)
- Piece representation:
  - "r" = red man, "R" = red king
  - "w" = white man, "W" = white king
  - "_" = empty square
- Player names: "red", "white"

## External Dependencies

- Standard library only (no external packages required)
