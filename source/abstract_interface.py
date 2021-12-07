from abc import ABC, abstractmethod

# TODO: Разработать абстрактный класс интерфейса взаимодействия с пользователем.
class AbstractUserInterface(ABC):
    @abstractmethod
    def get_game_mode(self) -> int:
        pass
    @abstractmethod
    def create_board(self) -> object:
        pass
    @abstractmethod
    def show_board(self) -> None:
        pass
    @abstractmethod
    def create_players(self) -> tuple:
        pass
    @abstractmethod
    def get_player_step(self, player: object, free_steps: tuple) -> None:
        pass
    @abstractmethod
    def get_board_size(self) -> int:
        pass
    @abstractmethod
    def chek_winner(self) -> None:
        pass
    @abstractmethod
    def show_score(self) -> None:
        pass
    @abstractmethod
    def repeat_game(self) -> bool:
        pass