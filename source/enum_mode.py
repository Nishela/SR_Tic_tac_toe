__all__ = (
    'ModeEnum',
)

from enum import Enum, unique


@unique
class ModeEnum(Enum):
    one_player = 1
    two_players = 2
    comp_vs_comp = 3
