def firstNotRepeatingCharacter(s):
    aux = {}
    for x in range(len(s)):
        if s[x] not in aux:
            aux.update({s[x]:1})
        else:
            aux.update({s[x]:aux[s[x]]+1})
    print(aux)
    return "_" if 1 not in aux.values() else [x for x in aux.keys() if aux[x] == 1][0]

if __name__ == '__main__':
	print(firstNotRepeatingCharacter('abcdefghijklmnopqrstuvwxyziflskecznslkjfabe'))