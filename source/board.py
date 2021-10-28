__all__ = (
    'BoardSizeError',
    'Bord'
)

from collections import defaultdict
from functools import reduce

from .utils import some

class BoardSizeError(Exception):
    pass

class StepError(Exception):
    pass

class Bord:
    def __init__(self, size: int):
        if (not size & 1) or (size < 3):
            raise BoardSizeError
        self.size = size
        self.all_steps = set((n, m) for n in range(size) for m in range(size))
        self.players_steps = defaultdict(set, n=set())

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
# TODO: сделать метод, который печатает в терминал ASCII доску.
# TODO: создать ошибку о конце вариантов ходов (ничья). На доске нет свободных ходов.
# TODO: продумать, спроектиросовтаваить план класса пользователя (игрока). Игрока 2 - комп+челб чел+чел. Разработать методику (что будет делать пользователь)