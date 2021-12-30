from abc import ABC, abstractmethod
from enum import Enum


class AbstractUserInterface(ABC):
    @property
    @abstractmethod
    def board(self) -> object:
        pass

    @property
    @abstractmethod
    def mode(self) -> Enum:
        pass
    
    @property
    @abstractmethod
    def player_1(self) -> object:
        pass

    @property
    @abstractmethod
    def player_2(self) -> object:
        pass

    @abstractmethod
    def get_game_mode(self) -> Enum:
        pass

    @abstractmethod
    def show_board(self) -> None:
        pass

    @abstractmethod
    def create_players(self, **kwargs: str) -> tuple:  # [object, object]:
        pass

    @abstractmethod
    def get_player_step(self, player: object, free_steps: tuple) -> None:  # [tuple[int, int], ...]) -> None:
        pass

    @property
    @abstractmethod
    def get_board_size(self) -> int:
        pass

    @abstractmethod
    def congrat(self) -> None:
        pass

    @abstractmethod
    def show_score(self) -> None:
        pass

    @abstractmethod
    def repeat_game(self) -> bool:
        pass
