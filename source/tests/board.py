from ..board import Board, BoardSizeError, StepError, WinnerError, NoFreeStepsError

__all__ = (
    'board_init_test',
    'board_step_test',
    'winner_test',
    'show_board_test',
    'free_steps_test',
)

TESTCASESINIT = (
    (0, False),
    (1, False),
    (2, False),
    (3, True),
    (4, False),
    (5, True),
    (6, False)
)


def board_init_test():
    for itm in TESTCASESINIT:
        result = True
        try:
            board = Board(itm[0])
        except BoardSizeError:
            result = False
        assert itm[1] is result, f'size={itm[0]}'


TESTCASESTEP = (
    (((0, 0), 'X'), True),
    (((2, 1), 'Y'), True),
    (((0, 1), 'X'), True),
    (((100, 1), 'X'), False),
    (((0, 2), 'X'), True)
)


def board_step_test():
    board = Board(3)
    for itm in TESTCASESTEP:
        result = True
        try:
            board.add_step(*itm[0])
        except StepError:
            result = False
        assert itm[1] is result, f'step={itm[0]}'


TESTCASEWINNER = (
    ((((0, 0), (2, 1), (1, 1)), 'X'), False),
    ((((0, 1), (1, 2), (0, 2)), 'Y'), False),
    ((((0, 0), (0, 1), (0, 2), (1, 1)), 'X'), True)
)


def winner_test():
    board = Board(3)
    for itm in TESTCASEWINNER:
        board.players_steps = {itm[0][1]: set(itm[0][0])}
        result = True
        try:
            board.winner()
        except WinnerError:
            result = False
        assert itm[1] is result


TESTCASESHOW = (
    ((((0, 0), (2, 1), (1, 1)), 'X'), True),
    ((((0, 1), (1, 2), (0, 2)), 'Y'), True),
)

def show_board_test():
    board = Board(3)
    board.players_steps = {itm[0][1]: set(itm[0][0]) for itm in TESTCASESHOW}
    result = True
    board.show_board()
    assert result


TESTCASENOFREESTEPS = (
    (((0, 0), 'X'), False),
)

def free_steps_test():
    board = Board(3)
    board.all_steps = set()
    result = True
    for itm in TESTCASENOFREESTEPS:
        try:
            board.add_step(*itm[0])
        except NoFreeStepsError:
            result = False
        assert itm[1] == result