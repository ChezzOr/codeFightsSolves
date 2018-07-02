def boxBlur(image):
    newImg = []
    height = len(image)
    wide = len(image[0])
    for row in range(1, height - 1, 1):
        newRow = []
        for column in range(1, wide - 1, 1):
            newRow.append(filterOp(image, row, column))
        newImg.append(newRow)
    return newImg

def filterOp(image, row, column):
    sum = 0
    for y in range(-1, 2):
        for x in range(-1, 2):
            sum += image[row + x][column + y]
    return int(sum / 9)
        