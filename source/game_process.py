from .board import Board
from .errors import NoFreeStepsError
from .player import Player
from enum import Enum
from .decorators import errors_catcher


class GameProcess:
    def __init__(self, user_interface, board, player_1, player_2):
        self.user_interface = user_interface
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.start_game = None

    @staticmethod
    def create_players(mode: Enum) -> tuple[object, object]:
        player_1 = Player('X', is_human=True if mode.value < 2 else False)
        player_2 = Player('O', is_human=True if mode.value == 2 else False)
        return player_1, player_2

    @staticmethod
    @errors_catcher
    def create_board(interface):
        size = interface.get_board_size()
        return Board(size)
    
    @classmethod
    def make_game(cls, interface_cls):
        interface = interface_cls()
        mode = interface.get_game_mode()
        player_1, player_2 = cls.create_players(mode)
        board = cls.create_board(interface)
        return cls(interface, board, player_1, player_2)

    @errors_catcher
    def run(self):
        self.start_game = True
        first_player_flag = True
        self.user_interface.show_board(self.board)
        while self.start_game:
            player = self.player_1 if first_player_flag else self.player_2
            try:
                step = self.user_interface.get_player_step(player, self.board.free_steps)
                self.board.add_step(step, player.symbol)
                self.user_interface.show_board(self.board)
                first_player_flag = False if player is self.player_1 else True
                if (winner := self.board.winner())[1]:
                    self.user_interface.congratulation(winner[0])
                    player.score += 1
                    self.user_interface.show_score(self.player_1, self.player_2)
                    self.start_game = False
                    break
            except NoFreeStepsError:
                self.user_interface.draw()
                self.start_game = False
                break
