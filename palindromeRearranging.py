def palindromeRearranging(inputString):
    dictionary = {}
    for x in inputString:
        if x not in dictionary.keys():
            dictionary.update({x:1})
        else:
            dictionary.update({x:dictionary[x]+1})

    flag == False
    for value in dictionary.values():
        if value % 2 == 1:
            if flag == True:
                return False
            flag = True
    return True