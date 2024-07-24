from dataclasses import dataclass
from typing import override

from form import Form
from mesurable import Mesurable1D


@dataclass(kw_only=True)
class Segment(Form, Mesurable1D):
    """class representing a segment with its 2 ends"""

    @override
    def translate(self, delta_x: float, delta_y) -> None:
        raise NotImplementedError

    @override
    def length(self) -> float:
        raise NotImplementedError

