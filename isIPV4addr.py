import _thread

def isIPv4Address(inputString):
    blocks = []
    for x in range(4):
        if x == 3:
            aux = inputString
        else:
            aux = inputString[:inputString.find('.')]
        try:
            if (len(aux) >= 4 or len(aux) <= 0) or ( int(aux) > 255 or int(aux) < 0 ):
                return False
            elif x != 3:
                inputString = inputString[inputString.find('.')+1 : ]
        except:
            return False
        #print(inputString)
    return True

def threading_func(input, ip):
    assert(isIPv4Address(ip) == input , "Faul on:"+ip)

def testCases():
    for a in range(-1, 258):
        for b in range(-1, 258):
            for c in range(-1, 258):
                for d in range(-1, 258):
                    ipstr = str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d)
                    if a < 0 or b < 0 or c < 0 or d < 0:
                        try:
                            _thread.start_new_thread(threading_func, (False, ipstr, ))
                        except:
                            print("Error: unable to start thread")
                    elif a > 255 or b > 255 or c > 255 or d > 255:
                        try:
                            _thread.start_new_thread(threading_func, (False, ipstr, ))
                        except:
                            print("Error: unable to start thread")
                    else:
                        try:
                            _thread.start_new_thread(threading_func, (True, ipstr, ))
                        except:
                            print("Error: unable to start thread")

if __name__ == '__main__':
    testCases()    