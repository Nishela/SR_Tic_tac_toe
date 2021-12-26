# TODO: Создать класс графического интерфейса в тестах.
from source import GameFactory, TerminalInterface, GameModeError, BoardSizeError, Board
import sys

TESTCASEGAMEMODE = (
    (1, True),
    (2, True),
    (3, False),
    ('a', False),
)


def test_get_game_mode():
    factory = GameFactory()
    for case in TESTCASEGAMEMODE:
        result = True
        try:
            factory.game_mode(case[0])
        except GameModeError:
            result = False
        assert case[1] is result, f'mode={case[0]}'


TESTCASEBOARDSIZE = (
    (1, True),
    ('a', False),
    (3, True),
    (10.57, False),
    ('name', False),
    (6, True),
)


def test_get_board_size():
    terminal_int = TerminalInterface()
    for itm in TESTCASEBOARDSIZE:
        result = True
        try:
            with open('test.txt', 'w', encoding='utf-8') as f:
                f.write(str(itm[0]))
            file = open('test.txt', 'r', encoding='utf-8')
            sys.stdin = file
            terminal_int.get_board_size
        except EOFError:
            result = False
        file.close()
        assert itm[1] is result, f'size={itm[0]}'


TESTCASECREATEBOARD = (
    (1, False),
    (3, True),
    (6, False),
    (5, True),
)


def test_create_board():
    terminal_int = TerminalInterface()
    for itm in TESTCASECREATEBOARD:
        result = True
        try:
            with open('test.txt', 'w', encoding='utf-8') as f:
                f.write(str(itm[0]))
            file = open('test.txt', 'r', encoding='utf-8')
            sys.stdin = file
            board = terminal_int.create_board()
        except EOFError as exc:
            result = False
        file.close()
        assert itm[1] is result, f'size={itm[0]}'


TESTCASECREATEPLAYERS = (
    (1, 'player_1', True),
    # (2, True),
    (3, 'player_1', False),
    (7, 'player_1', False),
)


def test_create_players():
    terminal_int = TerminalInterface()
    for itm in TESTCASECREATEPLAYERS:
        result = True
        try:
            with open('test.txt', 'w', encoding='utf-8') as f:
                f.write(str(itm[1]))
            file = open('test.txt', 'r', encoding='utf-8')
            sys.stdin = file
            p_1, p_2 = terminal_int.create_players()
        except EOFError:
            result = False
        file.close()
        assert itm[1] is result, f'mode={itm[0]}'

test_create_players()


