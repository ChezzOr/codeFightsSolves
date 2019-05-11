def reverseInParentheses(inputString):
    '''break in strings
        recursion if ( then recursive until )
    '''
    return recursive(inputString, 0, len(inputString))

            
def recursive(inputS, start, end):
    aux = ''
    x = start
    while x < end:
        if inputS[x] == '(':
            recS = ''
            recS= recursive(inputS, x + 1, end)
            #print(recS[0])
            aux += recS[0]
            x = recS[1]
        elif inputS[x] == ')':
            x += 1
            return [aux[::-1], x]
        else:
            aux += inputS[x]
            x += 1
    #print(aux)
    return aux