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


#TODO: удалить этот класс и переписать все зависимости от него.
class GameFactory:

    @staticmethod
    def create_players(mode: object, player1_name=None, player2_name=None) -> tuple:#[object, object]:
        player_1 = Player('X', name=player1_name, is_human=True if mode.value < 2 else False)
        player_2 = Player('O', name=player2_name, is_human=True if mode.value == 2 else False)
        return player_1, player_2

    # TODO: унести принты в терминал интерфейс!
    @staticmethod
    def try_step(board: object, player: object, free_steps: tuple) -> None:
        print(f'Ход игрока {player.name} {player.symbol}')
        board.add_step(player.do_step(free_steps), player.symbol)

