def rowProcess(row, size):
    aux = row[0]
    for idx ,column in enumerate(row):
        if idx == size and column > aux:
            return True
        if column > aux or idx == 0 :
            aux = column
        else:
            break
    return False


def almostIncreasingSequence(sequence):
    size = len(sequence) - 2

    if len(sequence) == 2:
        return True

    for idx, x in enumerate(sequence):
        aux = []
        for idy, y in enumerate(sequence):
            if idx != idy:
                aux.append(y) 
        if rowProcess(aux, size) == True:
            return True

    return False

def testCases():
    print(almostIncreasingSequence([1, 3, 2, 1]) )#f
    print(almostIncreasingSequence([10, 1, 2, 3, 4, 5]) )#t
    print(almostIncreasingSequence([1, 3, 2]) ) #t
    print(almostIncreasingSequence([1, 2, 3, 4, 99, 5, 6]) )#t 
    print(almostIncreasingSequence([123, -17, -5, 1, 2, 3, 12, 43, 45]) )#t
    print(almostIncreasingSequence([1, 2, 5, 3, 5]) )#t
    print(almostIncreasingSequence([10, 1, 2, 3, 4, 5, 6, 1]) )#f
    print(almostIncreasingSequence([1 ,2 ,1 ,2]))#f

if __name__ == '__main__':
    testCases()
    #print(almostIncreasingSequence([1, 1]))    
