from .errors import GameModeError, WinnerError, BoardSizeError, StepError, RepeatGameError
import functools

errors_mapper = {
    GameModeError: lambda: print('Выбран некоррентный режим игры, попробуй еще. ERROR'),
    BoardSizeError: lambda: print('Нужно ввести целое нечетное число, которое больше двух! ERROR'),
    StepError: lambda: print('Некорректные координаты x, y. Попробуй еще: '),
    ValueError: lambda: print('Некорректный ввод. ERROR'),
    WinnerError: lambda: None,
    RepeatGameError: lambda: print('Введи "Y" или "N"'),
}

def errors_catcher(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        while True:
            try:
                result = func(*args, **kwargs)
                break
            except tuple(errors_mapper) as exc:
                function = errors_mapper.get(exc.__class__)
                if not function:
                # if function := errors_mapper.get(exc.__class__) is None:
                    raise exc
                function()
        return result

    return wrap
