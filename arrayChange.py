def arrayChange(inputArray):
    pivot = inputArray[0]
    augment = 0
    for x in range(len(inputArray)):
        if x > 0:
            if inputArray[x] <= pivot:
                aux = pivot - inputArray[x] + 1
                pivot = inputArray[x] + aux
                augment += aux
            else:
                pivot = inputArray[x]
    return augment   