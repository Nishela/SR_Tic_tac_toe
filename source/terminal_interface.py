from source import Board
from .abstract_interface import AbstractUserInterface
from .game import GameFactory
from .errors import RepeatGameError
from .decorators import errors_catcher
from .enum_mode import ModeEnum



# TODO: Разработать на основе абстр класса интерфейса класс взаимодействия с пользователе через терминал.
class TerminalInterface(AbstractUserInterface):
    board = None
    mode = None
    player_1 = None
    player_2 = None

    @errors_catcher
    def get_game_mode(self):
        print(f'Выбери режим игры!')
        for itm in ModeEnum:
            #TODO: отформатировать name
            #string. snakecase to text
            print(f'{itm.name} --> {itm.value}')
        mode_tmp = int(input('>> '))
        self.mode = ModeEnum(mode_tmp)
        return self.mode

    @property
    @errors_catcher
    def get_board_size(self):
        board_size = input('Введи размер доски (целое нечетное число): ')
        return int(board_size)

    def show_board(self):
        print(self.board)

    # TODO: удалить этот класс и переписать все зависимости от него.
    @errors_catcher
    def get_player_step(self, player, free_steps):
        return self.__factory.try_step(self.board, player, free_steps)

    def congrat(self, winner):
        print(f'Поздравляем игрока "{winner}"! Он выиграл!')
        
    def show_score(self):
        print(f'{self.player_1.name} : {self.player_1.score}\n{self.player_2.name} : {self.player_2.score}')

    @staticmethod
    @errors_catcher
    def repeat_game():
        repeat = input('Еще разок? (Y/N): ')
        if repeat == 'Y':
            return True
        elif repeat == 'N':
            return False
        raise RepeatGameError
