
import pytest
from circle import Circle
from point import Point


@pytest.fixture
def circle_c(point_a):
    return Circle(name="C", radius=10.0, center=point_a)

def test_surface(circle_c):
    surface = circle_c.surface()
    assert surface == 314.1592653589793

def test_perimter(circle_c):
    perimeter = circle_c.perimeter()
    assert perimeter == 62.83185307179586