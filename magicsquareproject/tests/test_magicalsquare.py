"""simple tests with pytest"""
from magicalsquare import is_magic


def test_square_ok_3():
    square = [
        [2, 7 , 6],
        [9, 5 , 1],
        [4, 3 , 8]
    ]
    assert is_magic(square)


def test_square_ko_row_3():
    square = [
        [8,9,6],
        [3,5,7],
        [4,1,2]
    ]
    assert not is_magic(square)
    