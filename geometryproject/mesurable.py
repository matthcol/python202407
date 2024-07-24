from abc import ABC, abstractmethod


class Mesurable1D(ABC):
    @abstractmethod
    def length(self) -> float:
        pass


class Mesurable2D(ABC):
    @abstractmethod
    def surface(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass