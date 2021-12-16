# TODO: Создать класс графического интерфейса в тестах.
from source import GameFactory, TerminalInterface, GameModeError, BoardSizeError
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
	(1.154, False),
	(10, True),
)
def test_get_board_size():
	terminal_int = TerminalInterface()
	with open('test.txt', 'r+', encoding='utf-8') as sys.stdin:
		for line in TESTCASEBOARDSIZE:
			sys.stdin.write(f'{line[0]}\n')
		for _ in sys.stdin.readlines():
			terminal_int.get_board_size

	
print(test_get_board_size())