# UI Module Design

## Overview

The `ui.py` module implements the `UI` class for terminal-based user interaction in the Checkers CLI game. It handles board display, move input parsing, and message output.

## Implementation Details

### Coordinate System Mapping

The UI module translates between alphanumeric notation and internal coordinates:

- **Notation**: "e6" where column a-h (left-to-right) and row 1-8 (bottom-to-top)
- **Internal coordinates**: (row, col) where row 0-7 (top-to-bottom), col 0-7 (left-to-right)

**Mapping rules:**
- Column a-h → col 0-7: `col = ord(letter) - ord('a')`
- Row 1-8 → row 7-0: `row = 8 - row_number`

**Example:** "e6f5" → (2, 4, 3, 4)
- e6: col=4 (e is 5th letter), row=2 (8-6=2)
- f5: col=5 (f is 6th letter), row=3 (8-5=3)

### Methods

#### `display_board(board)`
Prints the board using the Board's `display()` method. Relies on Board to provide the formatted string representation.

#### `parse_move(move_str)`
Parses move notation like "e6f5" into a tuple `(from_row, from_col, to_row, to_col)`.

**Validation assumptions:**
- Input must be exactly 4 characters
- First two chars: source square (e.g., "e6")
- Last two chars: destination square (e.g., "f5")
- Columns: a-h (case-insensitive)
- Rows: 1-8

#### `get_player_input(player)`
Prompts the current player for a move using standard input. Returns the raw input string.

#### `display_message(msg)`
Prints a message to the terminal. Used for general game messages and instructions.

#### `display_winner(winner)`
Announces the game winner in the format "{winner} wins!".

## Dependencies

- Uses standard library only (input, print)
- Works with Board class from board.py

## Design Decisions

1. **No validation in parse_move**: The parser assumes valid input. Validation is handled by the Game class when executing moves.

2. **Simple display_board**: Delegates actual board formatting to Board.display() to maintain separation of concerns.

3. **No error handling**: The module assumes valid input and normal operation. Error handling would be added in main.py or game.py.

## Future Extensions

- Input validation with error messages
- Move history display
- Hint system for valid moves
- Color output for terminal enhanced display
