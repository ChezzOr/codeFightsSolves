def avoidObstacles(inputArray):
    for y in range(40):
        x = 0
        while x < 40:
            x += y + 1
            if x in inputArray:
                break
            if x >= 40:
                return y + 1
                
        
            