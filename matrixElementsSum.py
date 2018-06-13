def matrixElementsSum(matrix):
    ''' mark each column if 0, add if not 0 or not column in array '''
    ghost = []
    result = 0
    for row in matrix:
        for idc, column in enumerate(row):
            if column == 0:
                if idc not in ghost:
                    ghost.append(idc)
            elif idc not in ghost:
                result += column
    return result