from dataclasses import dataclass, field
import math
from typing import override
from .form import Form
from .mesurable import Mesurable2D
from .point import Point

@dataclass(kw_only=True)
class Circle(Form, Mesurable2D):
    """class representing a Circle with its radius and its center
    """
    
    center: Point = field(default_factory=Point)
    radius: float = 1.0
    
    @property
    def diameter(self) -> float:
        return self.radius * 2.0
    
    @diameter.setter
    def diameter(self, value: float) -> None:
        self.radius = value / 2.0
    
    @override
    def surface(self) -> float:
        return math.pi * self.radius**2
    
    @override
    def perimeter(self) -> float:
        return 2.0 * math.pi * self.radius

    @override
    def translate(self, delta_x: float, delta_y) -> None:
        self.center.translate(delta_x, delta_y)
