from circle import Circle
from form import Form
from point import Point
from polygon import Polygon
from weightedpoint import WeightedPoint


forms: list[Form] = [
    Point(name="A", x=1.0, y=3.0),
    Point(name="B", x=1.0, y=2.0),
    Point(name="D", x=4.0, y=2.0),
    WeightedPoint(name="W", x=4.0, y=2.0, weight=5.0),
    Circle(name="C1"),
    Polygon(name="ABCD"),
    Polygon(name="ABC")
]
print(forms)

for f in forms:
    print(f)
    print(f.name)  # mypy ok, forms: list[Form]
    f.translate(1, -1)
    print(f)
    print()


for f in forms:
    print(f.name)
    match f:
        case WeightedPoint():
            print("\t This is a weighted point:", f)
            print("\t", f.x, f.y, f.weight)
        case Point(): 
            print("\t This is a point:", f)
            print("\t", f.x, f.y)
        case Circle():
            print("\t This is a circle", f)
            print("\t", f.radius, f.center)
        case Polygon():
            print("\t This is a polygon", f)
            print("\t", f.vertices)
        case _:
            print("\t Unknown form:", f) 