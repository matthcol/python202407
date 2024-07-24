from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(kw_only=True)
class Form(ABC):
    """class generalizing geometry forms (point, circle, segment, polygon, ...)"""

    name: str | None = None 

    @abstractmethod
    def translate(self, delta_x: float, delta_y) -> None:
        pass


# if __name__ == '__main__':
#     f = Form() # mypy error, dynamic error: cannot instantiate
#     f.translate(12, 15)