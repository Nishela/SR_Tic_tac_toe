from source import NoFreeStepsError, WinnerError

class GameProcess:
    def __init__(self, user_interface, board, player_1, player_2):
        self.user_interface = user_interface
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2

    def _run(self):
        self.start_game = True
        self.first_player_flag = True
        print(self.board)
        while self.start_game:
            player = self.player_1 if self.first_player_flag else self.player_2
            try:
                self.user_interface.get_player_step(player, self.board.free_steps)
                print(self.board)
                self.first_player_flag = False if player is self.player_1 else True
                self.user_interface.chek_winner()
                player.score += 1
                self.user_interface.show_score()
                self.start_game = False
                break
            except NoFreeStepsError:
                print('Победила дружба!')
                self.start_game = False
                break
            except WinnerError:
                pass
