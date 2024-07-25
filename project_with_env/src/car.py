from dataclasses import dataclass


@dataclass
class Car:
    model: str
    power: int
    color: str