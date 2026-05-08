from src.ui import UI
from src.game import Game


def main():
    ui = UI()
    game = Game()

    while not game.is_game_over():
        ui.display_board(game._board)
        move_str = ui.get_player_input(game.current_player)
        from_row, from_col, to_row, to_col = ui.parse_move(move_str)
        if not game.execute_move(from_row, from_col, to_row, to_col):
            ui.display_message("Invalid move")
            continue

    ui.display_winner(game._board.check_winner())


if __name__ == "__main__":
    main()
