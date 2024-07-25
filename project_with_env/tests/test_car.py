import pytest

from car import Car

@pytest.fixture
def car0():
    return Car("Fiat 500", 150, 'rose')

def test_init(car0):
    assert car0.model == "Fiat 500"
    assert car0.power == 150
    assert car0.color == 'rose'
