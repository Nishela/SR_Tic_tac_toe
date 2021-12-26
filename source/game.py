__all__ = (
    'GameFactory',
)
'''
- напечатать строку по шаблону (ход игрока, имя, символ)
- напечатать доску на экране
- запросить у игрока запросить ход
- сообщить о неверном ходе
- проверка победителя
- передача хода след игроку, либо поздравляем победителя
- обработка ничьи
'''

from .player import Player
from .errors import GameModeError
from .enum_mode import EnumMode


class GameFactory:
    # MODES = {
    #     1: 'One player',
    #     2: 'Two players',
    # }

    def game_mode(self, mode: int) -> object:
        for itm in EnumMode:
            if mode == itm.value[0]:
                return itm
        raise GameModeError


    @staticmethod
    def create_players(mode: object) -> tuple[object, object]:
        player_1 = Player('X', is_human=True if mode.value[0] < 2 else False)
        player_2 = Player('O', is_human=True if mode.value[0] == 2 else False)
        return player_1, player_2

    @staticmethod
    def try_step(board: object, player: object, free_steps: tuple) -> None:
        print(f'Ход игрока {player.name} {player.symbol}')
        board.add_step(player.do_step(free_steps), player.symbol)

# TODO: В игре и во всех ее классах поддержать взаимодействие с пользователе посредством класса интерфейса.
