def sortByHeight(a):
    n = len(a)
    for x in range(n):
        for y in range(n - 1):
            if a[x] != -1 and a[x] < a[y]:
                a[x], a[y] = a[y], a[x]
    return a

def testCases():
    print(str(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180])))
    print(str(sortByHeight([4, 2, 9, 11, 2, 16])))
    print(str(sortByHeight([-1, -1, -1, -1, -1])))
    print(str(sortByHeight([-1, -1, 2, -1, 2, 1])))
    print(str(sortByHeight([23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3])))


if __name__ == '__main__':
    testCases()