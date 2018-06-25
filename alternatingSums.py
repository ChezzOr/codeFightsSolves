def alternatingSums(a):
    result = [0,0]
    for idx in range(len(a)):
        if idx % 2 == 0:
            result[0] += a[idx]
        else:
            result[1] += a[idx]
    return result