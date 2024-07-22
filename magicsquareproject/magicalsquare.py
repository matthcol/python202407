"""module magicalsquare

functions to check magicness of a square, generate magical square, etc. 
"""

#NB: PEP 8: Style Guide for Python Code
def is_magic(square):
    """check is a square is magic according to the following criteria:
    - all sums of rows are equals
    - all sums of columns are equals
    - all sums of 'diagonals' are equals
    - each number in the square is in range [0 - n^2] and used only once

    arguments:
    - square: square to check as a list of list of integers (or equivalent)

    return value: magicness of square (boolean)

    NB: magic sum is n(n^2 + 1)/2 with all these rules 
    """
    n = len(square)

    magic = True
    magic_sum = n*(n**2 +1)/2

    for line in square : 
        if not sum(line) == magic_sum :
            magic = False

    for i in range (n): 
        if not sum(line[i] for line in square) == magic_sum : 
            magic = False
    
    if not sum(square[i][i] for i in range (n)) == magic_sum :
        magic = False
        
    if not sum(square[i][-i-1] for i in range (n)) == magic_sum :
        magic = False   

    list_number = []
    for line in square : 
        for i in line : 
            if i not in list_number and 0 <= i <= n**2 : 
                list_number.append(i)
            else : 
                magic = False        
    return magic

