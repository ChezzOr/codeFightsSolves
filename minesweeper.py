def minesweeper(matrix):
    height = len(matrix) 
    width = len(matrix[0])
    newMatrix = [[0 for w in range(width)] for z in range(height)]
    for row in range(height):
        for column in range(width):
            if matrix[row][column] == True:
                if 0 < row < height - 1 and 0 < column < width - 1:
                    for x in range(-1, 2, 1):
                        for y in range(-1, 2, 1):
                            if x == y and y == 0:
                                continue
                            newMatrix[row+x][column+y] += 1
                elif row == 0 and column == 0:
                    for x in range(0, 2, 1):
                        for y in range(0, 2, 1):
                            if x == y and y == 0:
                                continue
                            newMatrix[row+x][column+y] += 1
                elif row == 0 and column == width - 1:
                    for x in range(0, 2, 1):
                        for y in range(-1, 1, 1):
                            if x == y and y == 0:
                                continue
                            newMatrix[row+x][column+y] += 1
                elif row == height - 1 and column == 0:
                    for x in range(-1, 1, 1):
                        for y in range(0, 2, 1):
                            if x == y and y == 0:
                                continue
                            newMatrix[row+x][column+y] += 1
                elif row == height - 1 and column == width - 1:
                    for x in range(-1, 1, 1):
                        for y in range(-1, 1, 1):
                            if x == y and y == 0:
                                continue
                            newMatrix[row+x][column+y] += 1
                elif row == 0 and  0 < column < width - 1:
                    for x in range(0, 2, 1):
                        for y in range(-1, 2, 1):
                            if x == y and y == 0:
                                continue
                            newMatrix[row+x][column+y] += 1
                elif  0 < row < height - 1 and column == 0:
                    for x in range(-1, 2, 1):
                        for y in range(0, 2, 1):
                            if x == y and y == 0:
                                continue
                            newMatrix[row+x][column+y] += 1
                elif row == height - 1 and  0 < column < width - 1:
                    for x in range(-1, 1, 1):
                        for y in range(-1, 2, 1):
                            if x == y and y == 0:
                                continue
                            newMatrix[row+x][column+y] += 1
                elif  0 < row < height - 1 and column == width - 1:
                    for x in range(-1, 2, 1):
                        for y in range(-1, 1, 1):
                            if x == y and y == 0:
                                continue
                            newMatrix[row+x][column+y] += 1
    return newMatrix

if __name__ == '__main__':
    print(minesweeper([[True,False,False,True], 
 [False,False,True,False], 
 [True,True,False,True]]))