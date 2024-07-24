import pytest
from point import Point

# NB: doc fixtures
# https://docs.pytest.org/en/stable/reference/fixtures.html#reference-fixtures

@pytest.fixture
def point_a():
    return Point(name="A", x=1.5, y= 3.25)