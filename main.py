from source import TerminalInterface, GameProcess


class TicTacToeTerminal:
    def __init__(self):
        self.game_process = GameProcess.make_game(TerminalInterface)

    def start_game(self):
        while True:
            self.game_process.run()
            if self.game_process.user_interface.repeat_game():
                self.game_process.board.players_steps.clear()
            else:
                break


if __name__ == '__main__':
    game = TicTacToeTerminal()
    game.start_game()
