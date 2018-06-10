def adjacentElementsProduct(inputArray):
    '''Linear search for biggest product'''
    res = -1001
    len_arr = len(inputArray) - 1
    for idx, x in enumerate(inputArray):
        if idx < len_arr:
            aux = x * inputArray[idx+1]
            res = aux if aux > res else res
    return res
