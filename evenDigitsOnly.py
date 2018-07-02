def evenDigitsOnly(n):
    while n > 0:
        if n % 2 != 0:
            return False
        n = (int)(n / 10)
        
    return True