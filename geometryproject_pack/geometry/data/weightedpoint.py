from dataclasses import dataclass

from .point import Point


@dataclass(kw_only=True)
class WeightedPoint(Point):
    """class representing a weighted point.
    
    A weighted point is a 2D point with a weight"""

    weight: float = 1.0


if __name__ == '__main__':
    wp = WeightedPoint(name="W", x=4.5, y=7.25, weight=20.0)
    p = Point(name="P", x=1.5, y=11.25)
    d1 = p.distance(wp)
    d2 = wp.distance(p)
    d3 = wp.distance(wp)
    print(d1, d2, d3)
