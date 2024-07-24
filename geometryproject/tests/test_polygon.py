import pytest

from point import Point
from polygon import Polygon


@pytest.fixture
def pentagon_wikipedia() -> Polygon:
    return Polygon(
        vertices=[
            Point(x=1, y=6),
            Point(x=3, y=1),
            Point(x=7, y=2),
            Point(x=4, y=4),
            Point(x=8, y=5),
        ],
        name="P"
    )  

def test_surface(pentagon_wikipedia: Polygon):
    actual_surface = pentagon_wikipedia.surface()
    assert 16.5 == actual_surface
    
def test_perimeter(pentagon_wikipedia: Polygon):
    actual_perimeter = pentagon_wikipedia.perimeter()
    assert pytest.approx(24.308, 1E-3) == actual_perimeter