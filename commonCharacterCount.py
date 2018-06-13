def commonCharacterCount(s1, s2):
    '''If exact add 1, if not exact but single char add 1'''
    auxLen = 1
    maxLen = 1
    comp = []
    chars = []
    aux = s1[0]
    chars.append(aux)

    for idx, x in enumerate(s1[1:]):
        if x != aux[0]:
            if auxLen > maxLen:
                maxLen = auxLen
            if auxLen > 1:
                comp.append(aux)
            if x not in chars:
                chars.append(x)
            aux = x
            auxLen = 1
        elif x == aux[0] and idx == len(s1[1:]) - 1:
            auxLen += 1
            aux += x
            if auxLen > maxLen:
                maxLen = auxLen
            comp.append(aux)
        else:
            aux += x
            auxLen += 1
    #print(chars)
    #print(comp)
    #print(maxLen)
    aux = s2[0]
    res = 0
    flag = 0
    for x in s2[1:]:
        if aux[0] == x:
            aux += x
            #print(aux)
            if len(aux) > maxLen:
                aux = aux[1:]
            if maxLen > 1:
                if aux in comp:
                    res += 1
            elif flag == 0:
                res += 1
                flag = 1
        elif aux in comp:
            res += 1
            aux = x
            flag = 0
        elif len(aux) == 1 and aux in chars:
            res += 1
            aux = x
            flag = 0
        else:
            aux = x
            flag = 0
    if aux in chars and flag == 0:
        res += 1

    return res

def testCases():
    print(commonCharacterCount('aabcc', 'adcaa')) #3
    print(commonCharacterCount('a', 'aaa') ) #1
    print(commonCharacterCount('abca', 'xyzbac')) #3
    print(commonCharacterCount('zzzz', 'zzzzzzz')) #4

if __name__ == '__main__':
    testCases()