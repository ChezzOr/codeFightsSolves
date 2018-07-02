def alphabeticShift(inputString):
    out = ''
    for idx in range(len(inputString)):
        if ord(inputString[idx]) != 122:
            out += chr((ord(inputString[idx]) + 1))
        else:
            out += 'a'
    return out
