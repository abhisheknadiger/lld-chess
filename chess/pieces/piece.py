from abc import ABC, abstractmethod
class Piece(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def can_move(self):
        pass