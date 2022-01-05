from abc import ABC, abstractmethod
from enum import Enum


class AbstractUserInterface(ABC):

    @staticmethod
    @abstractmethod
    def get_game_mode() -> Enum:
        pass

    @staticmethod
    @abstractmethod
    def show_board(board: object) -> None:
        pass

    @staticmethod
    @abstractmethod
    def get_board_size() -> int:
        pass

    @abstractmethod
    def get_player_step(self, player: object, free_steps: [tuple[int, int], ...]) -> tuple:
        pass

    @staticmethod
    @abstractmethod
    def congratulation(winner: str) -> None:
        pass

    @staticmethod
    @abstractmethod
    def draw() -> None:
        pass

    @staticmethod
    @abstractmethod
    def show_score(player_1: object, player_2: object) -> None:
        pass

    @staticmethod
    @abstractmethod
    def repeat_game() -> bool:
        pass
