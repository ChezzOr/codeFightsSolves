def makeArrayConsecutive2(statues):
    '''Search for max and min, then compare size of array with difference between min and max'''
    min = 11
    max = -1
    for x in statues:
        if x > max:
            max = x
        if x < min:
            min = x
    return (max - min) - len(statues) + 1
