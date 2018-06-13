def allLongestStrings(inputArray):
    longStrings = []
    maxlen = 0
    for string in inputArray:
        if len(string) > maxlen:
            maxlen = len(string)
            longStrings = []
            longStrings.append(string)
        elif len(string) == maxlen:
            longStrings.append(string)
    return longStrings