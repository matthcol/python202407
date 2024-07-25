import pytest
import geometry as geo


@pytest.fixture
def point_b():
    return geo.Point(name="B", x=5.5, y= 0.25)

def test_distance(point_a, point_b):
    assert 5.0 == point_a.distance(point_b)

@pytest.mark.parametrize(
        ["x_a", "y_a", "x_b", "y_b", "expected_distance", "precision"],
        [
            (1.5, 3.25, 5.5, 0.25, 5.0, 1E-10),
            (1.5E3, 3.25E3, 5.5E3, 0.25E3, 5.0E3, 1E-7),
            (1.5E300, 3.25E300, 5.5E300, 0.25E300, 5.0E300, 1E290),
            (1.5E-300, 3.25E-300, 5.5E-300, 0.25E-300, 5.0E-300, 1E-310),
        ]
)
def test_distance_scale(x_a, y_a, x_b, y_b, expected_distance, precision):
    pt_a = geo.Point(name="A", x=x_a, y=y_a) 
    pt_b = geo.Point(name="B", x=x_b, y=y_b) 
    assert pytest.approx(expected_distance, precision) == pt_a.distance(pt_b)