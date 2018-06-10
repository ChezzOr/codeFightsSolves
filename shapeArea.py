def shapeArea(n):
    '''Pattern, easier to spot with graphical representation 
    1 5 13 25
    1 = 1
    2 ^ 2 + 1 ^ 2 = 5
    3 ^ 3 + 2 ^ 2 = 13
    4 ^ 4 + 3 ^ 3 = 25
    '''
    return (n * n) + ((n - 1) * (n - 1)) if n > 1 else 1 