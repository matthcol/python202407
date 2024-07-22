from magicalsquare import is_magic


square1 = [
    [2, 7 , 6],
    [9, 5 , 1],
    [4, 3 , 8],
]

square2 = [
    [8,1,5],
    [3,5,7], 
    [4,9,2]]

for square in square1, square2:
    print(square)
    print("is magic:", is_magic(square))
    print()