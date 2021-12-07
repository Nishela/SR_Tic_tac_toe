import random
from .errors import StepError


class DoStepMixin:

    def do_step(self, free_steps):
        if self.is_human:
            return self._human_step()
        return self._bot_step(free_steps)

    def _bot_step(self, free_steps):
        return random.choice(free_steps)

    # TODO: обработка ошибки ввода пользователя
    def _human_step(self):
        step = input('Ваш ход - x, y: ')
        if all(x.isdigit() for x in step.split(',')):
            return tuple(int(x) for x in step.split(','))
        raise StepError


class NameMixin:

    def get_name(self):
        if self.is_human:
            return self._human_name()
        return self._bot_name()

    def _human_name(self):
        self.name = input(f'Игрок {self.symbol} Ваше имя: ')
        return self.name

    def _bot_name(self):
        self.name = 'R2D2'
        return self.name
