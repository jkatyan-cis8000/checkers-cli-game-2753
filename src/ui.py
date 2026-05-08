class UI:
    def display_board(self, board):
        print(board.display())

    def parse_move(self, move_str):
        from_col = ord(move_str[0].lower()) - ord('a')
        from_row = 8 - int(move_str[1])
        to_col = ord(move_str[2].lower()) - ord('a')
        to_row = 8 - int(move_str[3])
        return (from_row, from_col, to_row, to_col)

    def get_player_input(self, player):
        return input(f"{player}'s move: ")

    def display_message(self, msg):
        print(msg)

    def display_winner(self, winner):
        print(f"{winner} wins!")
