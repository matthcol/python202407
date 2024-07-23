"""Examples of fatorized tests"""
import pytest

from magicalsquare import is_magic

@pytest.mark.parametrize(
    ['squarename'], 
    [
        ('square3_ok',),
        ('square4_albrecht_durer',),
        ('square5_semi_diabolik',),
        ('square5_ok',),
        ('square8_general_cazalas',),
        ('square8_general_cazalas',),
        ('square8_willem_barink',),
        ('square12_willem_barink',),        
    ]
)
def test_is_magic_ok(squarename, request):
    square = request.getfixturevalue(squarename)
    assert is_magic(square)

@pytest.mark.parametrize(
    ['squarename'], 
    [
        ('square3_ko_row',),
        ('square3_ko_col',),
        ('square3_ko_diag',),
        ('square3_ko_diag_one',),
        ('square3_ko_diag_two',),
        ('square4_josep_maria_subirachs',), # doubles and magic sum = 33 instead of 34
        ('square8_benjamin_franklin',), # diagonals are not magic
        ('square3_ko_outOfRangeAbove',),        
        ('square3_ko_outOfRangeUnder',),        
        ('square3_ko_doubles',),        
    ]
)
def test_is_magic_ko(squarename, request):
    square = request.getfixturevalue(squarename)
    assert not is_magic(square)

@pytest.mark.parametrize(
    ['squarename'], 
    [
        ('square_ko_notSquare1d',),
        ('square_ko_notSquare3d',),
    ]
)
def test_is_magic_error(squarename, request):
    square = request.getfixturevalue(squarename)
    with pytest.raises(ValueError) as excinfo:
        _ = is_magic(square)
    assert "not a square" in str(excinfo.value)

