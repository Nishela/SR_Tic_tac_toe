from source import TerminalInterface, GameProcess, errors_catcher

class TicTacToeTerminal:
    #TODO: нужно инициализировать доску, графический интерфейс, игроков, сам процесс игры.
    def __init__(self):
        self.user_terminal_interface = TerminalInterface()
        self.board = self.user_terminal_interface.create_board()
        self.player_1, self.player_2 = self.user_terminal_interface.create_players()
        self.game_process = GameProcess(self.user_terminal_interface, self.board, self.player_1, self.player_2)


    def start_game(self):
        while True:
            self.game_process._run()
            if self.user_terminal_interface.repeat_game():
                self.board.players_steps.clear()
            else:
                break


if __name__ == '__main__':
    game = TicTacToeTerminal()
    game.start_game()
#TODO: Создать класс графического интерфейса в тестах.