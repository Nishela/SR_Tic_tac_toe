from source import Board
from .abstract_interface import AbstractUserInterface
from .game import GameFactory
from .errors import RepeatGameError
from .decorators import errors_catcher
from .enum_mode import EnumMode


# TODO: Разработать на основе абстр класса интерфейса класс взаимодействия с пользователе через терминал.
class TerminalInterface(AbstractUserInterface):
    board = None
    player_1 = None
    player_2 = None

    def __init__(self):
        self.__factory = GameFactory()

    @property
    @errors_catcher
    def get_game_mode(self):
        print(f'Выбери режим игры!')
        for itm in EnumMode:
            print(f'{itm.value[0]} --> {itm.value[1]}')
        mode = int(input('>> '))
        return self.__factory.game_mode(mode)

    @property
    @errors_catcher
    def get_board_size(self):
        board_size = input('Введи размер доски (целое нечетное число): ')
        return int(board_size)

    @errors_catcher
    def create_board(self):
        self.board = Board(self.get_board_size)
        return self.board

    def show_board(self):
        print(self.board)

    def create_players(self):
        self.player_1, self.player_2 = self.__factory.create_players(self.get_game_mode)
        return self.player_1, self.player_2

    @errors_catcher
    def get_player_step(self, player, free_steps):
        return self.__factory.try_step(self.board, player, free_steps)

    #TODO избавиться от возбуждения ошибки и сделать интерфейс возвращения bool
    def chek_winner(self):
        winner = self.board.winner()
        if winner[1]:
            print(f'Поздравляем игрока "{winner[0]}"! Он выиграл!')
        return winner[1]

    def show_score(self):
        print(f'{self.player_1.name} : {self.player_1.score}\n{self.player_2.name} : {self.player_2.score}')

    @staticmethod
    @errors_catcher
    def repeat_game() -> bool:
        repeat = input('Еще разок? (Y/N): ')
        if repeat == 'Y':
            return True
        elif repeat == 'N':
            return False
        raise RepeatGameError
