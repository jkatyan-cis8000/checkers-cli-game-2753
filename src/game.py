class Game:
    def __init__(self):
        from src.board import Board
        self._board = Board()
        self._current_player = "red"

    @property
    def current_player(self):
        return self._current_player

    def is_game_over(self):
        winner = self._board.check_winner()
        if winner:
            return True
        valid_moves = self.get_valid_moves(self._current_player)
        return len(valid_moves) == 0

    def get_valid_moves(self, player):
        moves = []
        for row in range(8):
            for col in range(8):
                piece = self._board.get_piece(row, col)
                if piece is None:
                    continue
                piece_color = "red" if piece.lower() == "r" else "white"
                if piece_color != player:
                    continue
                for to_row in range(8):
                    for to_col in range(8):
                        if self._board.is_valid_move(row, col, to_row, to_col, player):
                            moves.append((row, col, to_row, to_col))
        return moves

    def execute_move(self, from_row, from_col, to_row, to_col):
        if not self._board.is_valid_move(from_row, from_col, to_row, to_col, self._current_player):
            return False
        self._board.apply_move(from_row, from_col, to_row, to_col)
        self.switch_turn()
        return True

    def switch_turn(self):
        self._current_player = "white" if self._current_player == "red" else "red"
