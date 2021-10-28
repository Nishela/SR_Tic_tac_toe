from ..board import Bord, BoardSizeError, StepError

__all__ = (
    'board_init_test',
    'board_step_test',
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
            board = Bord(itm[0])
        except BoardSizeError:
            result = False
        assert itm[1] is result, f'size={itm[0]}'

TESTCASESTEP = (
    (((0, 0), 'X'), True),
    (((0, 1), 'Y'), True),
    (((0, 1), 'X'), False),
    (((100, 1), 'X'), False),
)

def board_step_test():
    board = Bord(3)
    for itm in TESTCASESTEP:
        result = True
        try:
            board.add_step(*itm[0])
        except StepError:
            result = False
        assert itm[1] is result, f'step={itm[0]}'