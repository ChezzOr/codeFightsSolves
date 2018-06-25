import math

def arrayMaximalAdjacentDifference(inputArray):
    pivot = inputArray[0]
    diff = -1
    for x in inputArray[1:]:
        aux1 = x
        aux2 = pivot
        if aux1 > aux2:
            dif = aux1 - aux2
        else:
            dif = aux2 - aux1
        if dif > diff:
            diff = dif
        pivot = x
    return diff

if __name__ == '__main__':
    print(arrayMaximalAdjacentDifference([-15,-14,-13,-12,-11,-10, 15]))