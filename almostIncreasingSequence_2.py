def almostIncreasingSequence(sequence):
    if len(sequence) == 2:
        return True

    pivot = sequence[0]
    flag = 0
    lastValue = pivot
    dictionary = {pivot:1}
    for idx, x in enumerate(sequence[1:]):
        '''print("Val: " + str(x))
        print("Piv: " + str(pivot))
        print("-----------------")'''
        
        if x in dictionary.keys():
            dictionary.update({x:2})
        else:
            dictionary.update({x:1})
        values = dictionary.values()

        rep = 0
        for val in values:
            if val == 2:
                rep += 1
            if rep > 1:
                return False
        
        if x > pivot and x > lastValue:
            lastValue = pivot
        else:
            if idx != 0:
                flag += 1
                pivot = lastValue
            else:
                flag += 1
                lastValue = x
        pivot = x
        if flag > 1:
            return False
    return True


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
    #testCases()
    print(almostIncreasingSequence([1, 2, 3, 4, 3, 6]))    
