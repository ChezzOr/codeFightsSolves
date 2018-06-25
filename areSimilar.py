def areSimilar(a, b):
    dict = {}
    for x in a:
        if x not in dict.keys():
            dict.update({x:1})
        else:
            dict.update({x:dict[x]+1})
    flag = 0
    for idx, x in enumerate(b):
        if a[idx] != b[idx]:
            flag += 1
            if flag >= 3:
                return False
        if x not in dict.keys():
            return False
        else:
            dict.update({x:dict[x]-1})
    for x in dict.values():
        if x != 0:
            return False
    return True

if __name__ == '__main__':
    print(areSimilar([1,2,1], [2,2,1]))