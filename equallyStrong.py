def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
        lefd = yourLeft - friendsLeft
        rigd = yourRight - friendsRight
        lfxd = yourLeft - friendsRight
        rgxd = yourRight - friendsLeft
        
        if lefd == rigd and rigd == 0:
                return True
        elif lfxd == rgxd and rgxd == 0:
                return True
        else: 
                return False