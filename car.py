from typing import cast
from functools import total_ordering

@total_ordering
class Car:
    """class representing a car with its model, power and color
    
        Example:
            car = Car(model='Fiat 500', color='rose', power=150)
    """

    # froze list of attributes
    __slots__ = ('model', 'color', 'power')

    # constructor
    def __init__(self, model: str, color: str | None = None, power: int | None = None):
        self.model = model
        self.color = color
        self.power = power

    # implementation of both repr and str builtin functions (if no __str__ definition)
    def __repr__(self) -> str:
        return f"Car(model={self.model}, color={self.color}, power={self.power})"
    

    def __str__(self) -> str:
        return f"{self.model} (color={self.color}, power={self.power})"
    

    # implementation of == and !=
    def __eq__(self, value: object) -> bool:
        # if type(value) is not Car:
        if not isinstance(value, Car):
            return NotImplemented
        other = cast(Car, value)
        return (self.model, self.color, self.power) == (other.model, other.color, other.power)
    
    # __lt__: <
    # __le__: <=
    # __gt__: >
    # __ge__: >=
    def __lt__(self, value: object) -> bool:
        if not isinstance(value, Car):
            return NotImplemented
        other = cast(Car, value)
        return (self.power, self.model, self.color) == (other.power, other.model, other.color)




if __name__ == '__main__':
    c = Car(model='Fiat 500')
    print(c)
    print(str(c))
    print(repr(c))
    print(c.model, c.color, c.power)
    