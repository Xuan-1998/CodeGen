import math

def getExponent(n, p):
    if p <= 1:
        print("ArgumentOutOfRange")
        return None
    exp = int(math.log(n, p))
    return exp
