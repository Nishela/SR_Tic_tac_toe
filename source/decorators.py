from .errors import GameModeError, WinnerError, BoardSizeError, StepError, RepeatGameError
import functools


def errors_catcher(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        while True:
            try:
                result = func(*args, **kwargs)
                break
            except GameModeError:
                print(f'Выбран некоррентный режим игры, попробуй еще. ERROR')
            except BoardSizeError:
                print(f'Нужно ввести целое нечетное число, которое больше двух! ERROR')
            except StepError:
                print(f'Некорректные координаты x, y. Попробуй еще: ')
            except ValueError:
                print(f'Некорректный ввод. ERROR')
            except WinnerError:
                pass
            except RepeatGameError:
                print('Введи "Y" или "N"')
        return result

    return wrap
