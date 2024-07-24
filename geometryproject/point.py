from dataclasses import dataclass
import math
from typing import override

from form import Form

#T = TypeVar('T', bound='Point')

@dataclass(kw_only=True)
class Point(Form):
    """class representing a 2D Point with its coordinates x, y
    """
    x: float = 0.0
    y: float = 0.0

    def distance(self, other: 'Point') -> float:
        return math.hypot(
            self.x - other.x,
            self.y - other.y
        )

    @override # since python 3.12
    def translate(self, delta_x: float, delta_y) -> None:
        self.x += delta_x
        self.y += delta_y  


# Wrong code (type error for argument)
# if __name__ == '__main__':
#     p = Point()
#     _ = p.distance(12)
if __name__ == '__main__':
    p = Point()
    print(p)