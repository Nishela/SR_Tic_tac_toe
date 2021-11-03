__all__ = (
    'BoardSizeError',
    'Board'
)

from collections import defaultdict
from functools import reduce

from .utils import horizont_combinations


class BoardSizeError(Exception):
    pass

class StepError(Exception):
    pass

class WinnerError(Exception):
    pass

class Board:
    def __init__(self, size: int):
        if (not size & 1) or (size < 3):
            raise BoardSizeError
        self.size = size
        self.all_steps = set((n, m) for n in range(size) for m in range(size))
        self.players_steps = defaultdict(set)

    @property
    def free_steps(self):
        return self.all_steps.difference({item for itm in self.players_steps.values() for item in itm})

    # @property
    # def free_steps_2(self):
    #     return reduce(lambda x, y: x & y, self.players_steps.values()) | self.all_steps

    def __step_validator(self, step):
        if step not in self.free_steps:
             raise StepError

    def add_step(self, step: tuple, player_symbol: str):
        self.__step_validator(step)
        self.players_steps[player_symbol].add(step)

# TODO: метод, который возвращает tuple(bool и символ игрока) победителя. Нужно найти выигрышную комбинацию и определить какой игрок ее достиг. Написать тест для этого метода
    def __combinations(self):
        horizont = horizont_combinations(tuple(self.all_steps), self.size)
        vertical = tuple(zip(*horizont))
        diagonal_1 = tuple(horizont[itm][itm] for itm in range(len(horizont)))
        diagonal_2 = tuple(horizont[idx][itm] for idx, itm in enumerate(range(len(horizont) - 1, -1, -1)))
        return horizont + vertical + (diagonal_1, diagonal_2)

    def winner(self):
        combinations = self.__combinations()
        for player in self.players_steps:
            for combo in combinations:
                if set(combo).intersection(self.players_steps[player]) == set(combo):
                    return True, player
        raise WinnerError

# TODO: сделать метод, который печатает в терминал ASCII доску.
# TODO: создать ошибку о конце вариантов ходов (ничья). На доске нет свободных ходов.
# TODO: продумать, спроектиросовтаваить план класса пользователя (игрока). Игрока 2 - комп+челб чел+чел. Разработать методику (что будет делать пользователь)