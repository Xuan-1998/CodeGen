import math

def getExponent(n, p):
    return math.ceil(math.log10(n) / math.log10(p))

n = int(input())
p = int(input())

exponent = getExponent(n, p)
print(exponent)
