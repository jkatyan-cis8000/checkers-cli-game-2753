class Board:
    def __init__(self):
        self._board = []
        self._initialize_board()

    def _initialize_board(self):
        for row in range(8):
            self._board.append([])
            for col in range(8):
                if (row + col) % 2 == 1:
                    if row > 4:
                        self._board[row].append("r")
                    elif row < 3:
                        self._board[row].append("w")
                    else:
                        self._board[row].append("_")
                else:
                    self._board[row].append("_")

    def display(self):
        lines = []
        for row in range(8):
            line = ""
            for col in range(8):
                line += self._board[row][col] + " "
            lines.append(line.strip())
        return "\n".join(lines)

    def get_piece(self, row, col):
        if not self.is_valid_square(row, col):
            return None
        return self._board[row][col]

    def is_valid_square(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def is_valid_move(self, from_row, from_col, to_row, to_col, player):
        if not self.is_valid_square(from_row, from_col) or not self.is_valid_square(to_row, to_col):
            return False

        piece = self._board[from_row][from_col]
        if piece == "_":
            return False

        piece_color = piece.lower()
        if piece_color != player[0]:
            return False

        if self._board[to_row][to_col] != "_":
            return False

        row_diff = to_row - from_row
        col_diff = to_col - from_col

        if abs(row_diff) != abs(col_diff):
            return False

        if piece == "r":
            if row_diff >= 0:
                return False
        elif piece == "w":
            if row_diff <= 0:
                return False

        if abs(row_diff) > 2:
            return False

        if abs(row_diff) == 2:
            mid_row = (from_row + to_row) // 2
            mid_col = (from_col + to_col) // 2
            mid_piece = self._board[mid_row][mid_col]
            if mid_piece == "_" or mid_piece.lower() == piece_color:
                return False

        return True

    def apply_move(self, from_row, from_col, to_row, to_col):
        piece = self._board[from_row][from_col]
        self._board[from_row][from_col] = "_"
        self._board[to_row][to_col] = piece

        if abs(to_row - from_row) == 2:
            mid_row = (from_row + to_row) // 2
            mid_col = (from_col + to_col) // 2
            self._board[mid_row][mid_col] = "_"

        if piece == "r" and to_row == 7:
            self._board[to_row][to_col] = "R"
        elif piece == "w" and to_row == 0:
            self._board[to_row][to_col] = "W"

    def is_king(self, row, col):
        piece = self._board[row][col]
        return piece in ("R", "W")

    def make_king(self, row, col):
        piece = self._board[row][col]
        if piece == "r":
            self._board[row][col] = "R"
        elif piece == "w":
            self._board[row][col] = "W"

    def check_winner(self):
        red_count = 0
        white_count = 0

        for row in range(8):
            for col in range(8):
                piece = self._board[row][col]
                if piece in ("r", "R"):
                    red_count += 1
                elif piece in ("w", "W"):
                    white_count += 1

        if red_count == 0:
            return "white"
        elif white_count == 0:
            return "red"
        return None
