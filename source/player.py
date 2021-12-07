__all__ = (
    'Player',
)
from .mixins import DoStepMixin, NameMixin

class Player(DoStepMixin, NameMixin):
    def __init__(self, symbol, name=None, is_human=False):
        self.is_human = is_human
        self.symbol = symbol
        self.name = name if name else self.get_name()
        self.score = 0
