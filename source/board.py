__all__ = (
    'Board',
)

from collections import defaultdict
from .errors import BoardSizeError, StepError, NoFreeStepsError


class Board:
    def __init__(self, size: int):
        if (not size & 1) or (size < 3):
            raise BoardSizeError
        self.size = size
        # self.all_steps = set((n, m) for n in range(size) for m in range(size))
        self.players_steps = defaultdict(set)

    @property
    def free_steps(self) -> tuple:
        free_moves = tuple((x, y) for x in range(self.size) for y in range(self.size) if
                           all((x, y) not in item for item in self.players_steps.values()))
        if free_moves:
            return free_moves
        raise NoFreeStepsError

    # @property
    # def free_steps_2(self):
    #     return reduce(lambda x, y: x & y, self.players_steps.values()) | self.all_steps

    def __step_validator(self, step):
        if (
                not all(map(lambda x: 0 <= x < self.size, step))
                or any(map(lambda x: step in x, self.players_steps.values()))
        ):
            raise StepError

    def add_step(self, step: tuple, player_symbol: str):
        self.__step_validator(step)
        self.players_steps[player_symbol].add(step)

    def __combinations(self):
        horizont = (((x, y) for x in range(self.size)) for y in range(self.size))
        vertical = (((y, x) for x in range(self.size)) for y in range(self.size))
        diagonal_1 = ((x, x) for x in range(self.size))
        diagonal_2 = ((x, y) for x, y in zip(range(self.size), range(self.size - 1, -1, -1)))
        for item in (horizont, vertical):
            yield from item

        for item in (diagonal_1, diagonal_2):
            yield item

    def winner(self):
        # combinations = self.__combinations()
        # for player in self.players_steps:
        #     for combo in combinations:
        #         tmp_combo = set(combo)
        #         if not tmp_combo.difference(self.players_steps[player]):
        #             return True, player
        # if tmp_combo.intersection(self.players_steps[player]) == tmp_combo:
        #     return True, player
        # return None, False

        var = (
            (win_combo, player, steps) for player, steps in self.players_steps.items()
            for win_combo in self.__combinations()
        )
        for combo, player, player_steps in var:
            if not set(combo).difference(player_steps):
                return player, True
        return None, False
        # raise WinnerError

    # def show_board(self):
    #     print(self)

    def __str__(self):
        matrix = [['-' for _ in range(self.size)] for _ in range(self.size)]
        for user, steps in self.players_steps.items():
            for x, y in steps:
                matrix[x][y] = user
        first_line = f'#{"".join(map(lambda x: f"#{x}", range(self.size)))}#'
        str_rows = "\n".join(map(lambda itm: f"{itm[0]}#{'|'.join(map(str, itm[1]))}#", enumerate(matrix)))
        result_str = f'{first_line}\n{str_rows}\n{"#" * len(first_line)}\n'
        return result_str
