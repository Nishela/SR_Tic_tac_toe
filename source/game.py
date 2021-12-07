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


class GameFactory:
    MODES = {
        1: 'Human VS Computer',
        2: 'Human VS Human',
    }

    # TODO: обработка ввода от пользователя
    def game_mode(self, mode: int) -> int:
        if mode in self.MODES:
            return mode
        raise GameModeError


    @staticmethod
    def create_players(mode):
        player_1 = Player('X', is_human=True)
        player_2 = Player('O', is_human=True if mode == 2 else False)
        return player_1, player_2

    @staticmethod
    def try_step(board: object, player: object, free_steps: tuple) -> None:
        print(f'Ход игрока {player.name} {player.symbol}')
        board.add_step(player.do_step(free_steps), player.symbol)

# TODO: В игре и во всех ее классах поддержать взаимодействие с пользователе посредством класса интерфейса.
