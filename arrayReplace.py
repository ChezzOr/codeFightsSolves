def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for idx in range(len(inputArray)):
        if inputArray[idx] == elemToReplace:
            inputArray[idx] = substitutionElem
    return inputArray
