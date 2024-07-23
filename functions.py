# Note: check hints with mypy

from typing import Sequence

def compute(x: int) -> int:
    return (x**2 + 1) // 2


def is_magic(
        square: Sequence[Sequence[int]],  #list[list[int]], 
        magic_sum: int | None = None, 
        double_allowed: bool = False
) -> bool:
    n = len(square)
    if magic_sum is None:
        magic_sum = n * (n**2 + 1) // 2

    return True

def f(a, *args, d = None, **kwargs):
    print('a:', a)
    print('args:', args)
    for arg in args:
        print('\t-', arg)
    print('d:', d)
    print('kwargs:', kwargs)
    for k, v in kwargs.items():
        match k:
            case 'color':
                print('color set to:', v)
            case 'width':
                print('width set to:', v)
            case _:
                # pass
                raise ValueError(f"Unknown arg: {k}")
    print()

def demo_f():
    f(1) # arg 'a' given by position
    f(1, 2, 3, 4) # arg 'a' = 1, arg 'args' = (2,3,4)
    f(1, 2, 3, 4, d="mardi")
    f(1, 2, 3, 4, color='red', d="mardi", width=25)
    # f() #  missing 1 required positional argument: 'a'
    values = 1,2,3,4
    arguments = { 'color': 'green', 'd': 34, 'width': 12 }
    f(*values, **arguments)

    #NB: zip(*square)

def demo_compute() -> None:
    # use case 1: ok
    y = compute(3)
    print("Result:", y)
    # use case 2: wrong type of argument: float instead of int
    r = compute(3.5)  # error with type checker mypy
    print("Result:", r)
    # use case 3: wrong type of argument: str instead of int
    t = compute("Pau") # error with type checker mypy
    print("Result:", t)


def demo_is_magique() -> None:
    ok1 = is_magic([[1, 2], [3, 4]], magic_sum=10)
    ok2 = is_magic([[1, 2], [3, 4]], magic_sum=15.5) # type error
    ok3 = is_magic([[1, 2], [3, 4]], magic_sum=10, double_allowed=True)
    ok4 = is_magic([[1, 2], [3, 4]], magic_sum=10, double_allowed="OK") # type error
    ok5 = is_magic([1, 2, 3, 4]) # type error
    ok6 = is_magic([[[1, 2], [3, 4]], [[4, 5], [6, 7]]]) # type error
    ok1 = is_magic(((1, 2), (3, 4)), magic_sum=10)

def demo_typing_containers() -> None:
    numbers: list[int] = [1, 2, 3]
    city_t: tuple[str, int, str] = ("Pau", 77_000, "64000")
    numbers_t: tuple[int, ...] = tuple(numbers)
    numbers2_t: tuple[int, ...] = ("Pau", 77_000, "64000")  # type error

if __name__ == '__main__':
    # demo_compute()
    # demo_is_magique()
    # demo_typing_containers()
    demo_f()