__all__ = (
    'EnumMode',
)

from enum import Enum, unique


@unique
class EnumMode(Enum):
    one_player = (1, 'One Player')
    two_players = (2, 'Two Players')
    comp_vs_comp = (3, 'Computer vs Computer')
