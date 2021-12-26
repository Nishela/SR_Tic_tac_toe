from abc import ABC, abstractmethod
from enum import Enum


# TODO: enum. Что это? определение режимов игры. нужны четкие структуры перечислений. Удобней чем словарь.
class AbstractUserInterface(ABC):
    # TODO: определить все публичные атрибуты. @property @abstract
    @property
    @abstractmethod
    def board(self) -> object:
        pass

    @property
    @abstractmethod
    def player_1(self) -> object:
        pass

    @property
    @abstractmethod
    def player_2(self) -> object:
        pass

    @property
    @abstractmethod
    def get_game_mode(self) -> Enum:
        pass

    @abstractmethod
    def create_board(self) -> object:
        pass

    @abstractmethod
    def show_board(self) -> None:
        pass

    @abstractmethod
    def create_players(self) -> tuple[object, object]:
        pass

    @abstractmethod
    def get_player_step(self, player: object, free_steps: tuple[tuple[int, int], ...]) -> None:
        pass

    @property
    @abstractmethod
    def get_board_size(self) -> int:
        pass

    @abstractmethod
    def chek_winner(self) -> bool:
        pass

    @abstractmethod
    def show_score(self) -> None:
        pass

    @abstractmethod
    def repeat_game(self) -> bool:
        pass
