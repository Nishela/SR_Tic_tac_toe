from .abstract_interface import AbstractUserInterface
from .errors import RepeatGameError
from .decorators import errors_catcher
from .mode_enum import ModeEnum


class TerminalInterface(AbstractUserInterface):

    @staticmethod
    @errors_catcher
    def get_game_mode():
        print(f'Выбери режим игры!')
        for itm in ModeEnum:
            print(f'{itm.value} --> {" ".join([item.capitalize() for item in itm.name.split("_")])}')
        mode_tmp = int(input('>> '))
        return ModeEnum(mode_tmp)

    @staticmethod
    @errors_catcher
    def get_board_size():
        board_size = input('Введи размер доски (целое нечетное число): ')
        return int(board_size)

    @staticmethod
    def show_board(board):
        print(board)

    @staticmethod
    @errors_catcher
    def get_player_step(player, free_steps):
        print(f'Ход игрока {player.name} {player.symbol}')
        return player.do_step(free_steps)

    @staticmethod
    def congratulation(winner):
        print(f'Поздравляем игрока "{winner}"! Он выиграл!')

    @staticmethod
    def draw():
        print('Победила дружба!')

    @staticmethod
    def show_score(player_1, player_2):
        print(f'{player_1.name} : {player_1.score}\n{player_2.name} : {player_2.score}')

    @staticmethod
    @errors_catcher
    def repeat_game():
        repeat = input('Еще разок? (Y/N): ')
        if repeat == 'Y':
            return True
        elif repeat == 'N':
            return False
        raise RepeatGameError
