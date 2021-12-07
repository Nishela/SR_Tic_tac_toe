from source import Board
from .abstract_interface import AbstractUserInterface
from .game import GameFactory
from .errors import WinnerError, RepeatGameError
from .decorators import errors_catcher


# TODO: Разработать на основе абстр класса интерфейса класс взаимодействия с пользователе через терминал.
class TerminalInterface(AbstractUserInterface):
    def __init__(self):
        self.factory = GameFactory()

    @property
    @errors_catcher
    def get_game_mode(self):
        print(f'Выбери режим игры!')
        for key, val in self.factory.MODES.items():
            print(f'{key} --> {val}')
        self.mode = int(input('>> '))
        return self.factory.game_mode(self.mode)

    @property
    @errors_catcher
    def get_board_size(self):
        self.board_size = input('Введи размер доски (целое нечетное число): ')
        return int(self.board_size)

    # TODO: создать доску.
    @errors_catcher
    def create_board(self):
        self.board = Board(self.get_board_size)
        return self.board

    # TODO: перенести в класс взаимодействия с пользователем
    def show_board(self):
        print(self.board)

    def create_players(self):
        self.player_1, self.player_2 = self.factory.create_players(self.get_game_mode)
        return self.player_1, self.player_2

    @errors_catcher
    def get_player_step(self, player, free_steps):
        return self.factory.try_step(self.board, player, free_steps)

    def chek_winner(self):
        self.winner = self.board.winner()
        if self.winner[1]:
            print(f'Поздравляем игрока "{self.winner[0]}"! Он выиграл!')
        else:
            raise WinnerError

    def show_score(self):
        print(f'{self.player_1.name} : {self.player_1.score}\n{self.player_2.name} : {self.player_2.score}')

    @errors_catcher
    def repeat_game(self) -> bool:
        repeat = input('Еще разок? (Y/N): ')
        if repeat == 'Y':
            return True
        elif repeat == 'N':
            return False
        raise RepeatGameError
