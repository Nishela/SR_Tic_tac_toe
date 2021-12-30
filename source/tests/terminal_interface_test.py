# TODO: Создать класс графического интерфейса в тестах.
from source import GameFactory, TerminalInterface, GameModeError, BoardSizeError, Board
import sys

TESTCASEGAMEMODE = (
    (1, True),
    (2, True),
    (3, True),
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

# test_get_game_mode()

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

# test_get_board_size()

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

# test_create_board()

TESTCASECREATEPLAYERS = (
    (1, 'player_1', None, True),
    (2, 'player_1', 'player_2', True),
    (3, 'player_1', 'player_2', True),
    (7, 'player_1', None, False),
    ('a', 'player_1', None, False),
)

def test_create_players():
    terminal_int = TerminalInterface()
    for itm in TESTCASECREATEPLAYERS:
        result = True
        try:
            with open('test.txt', 'w', encoding='utf-8') as f:
                f.write(str(itm[0]))
            file = open('test.txt', 'r', encoding='utf-8')
            sys.stdin = file
            terminal_int.get_game_mode()
            p_1, p_2 = terminal_int.create_players(player1_name=itm[1], player2_name=itm[2])
        except EOFError:
            result = False
        file.close()
        assert itm[-1] is result, f'mode={itm[0]}'

# test_create_players()

TESTCASEGETPLAYERSTEP = (
    (1, 'player_1', (0, 0), ((0, 0), (1, 1)), True),
    (1, 'player_1', (1, 1), ((0, 0), (1, 1)), True),
    (1, 'player_1', (4, 4), ((0, 0), (1, 1)), False),
    (1, 'player_1', (1, 2), ((0, 0), (1, 1)), False),
)

def test_get_player_step():
    terminal_int = TerminalInterface()
    for itm in TESTCASEGETPLAYERSTEP:
        result = True
        terminal_int.mode = GameFactory().game_mode(itm[0])
        terminal_int.board = Board(3)
        p_1, p_2 = terminal_int.create_players(player1_name=itm[1], player2_name='')
        try:
            with open('test.txt', 'w', encoding='utf-8') as f:
                f.write(','.join([str(x) for x in itm[2]]))
            file = open('test.txt', 'r', encoding='utf-8')
            sys.stdin = file
            terminal_int.get_player_step(p_1, itm[3])
        except EOFError:
            result = False
        file.close()
        assert itm[-1] is result, f'step={itm[2]}'

test_get_player_step()