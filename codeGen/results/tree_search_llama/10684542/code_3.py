import math

def getExponent(n, p):
    x = 0
    while n % p == 0:
        n //= p
        x += 1
    if x > int(math.log2(n)):
        return None
    return x
