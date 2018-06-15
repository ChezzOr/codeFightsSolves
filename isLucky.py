def isLucky(n):
    left = 0
    right = 0
    half = int(len(str(abs(n)))/2)
    laps = 1
    while n > 0:
        if laps > half:
            right += n % 10
        else:
            left += n % 10
        n = int(n / 10)
        laps += 1
    
    if left == right:
        return True
    else:
        return False

if __name__ == '__main__':
    isLucky(1230)