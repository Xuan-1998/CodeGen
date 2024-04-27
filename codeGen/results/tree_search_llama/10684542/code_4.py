def getExponent(n, p):
    exponent = 0
    while pow(p, exponent) <= n:
        exponent += 1
    return exponent - 1

n, p = map(int, input().split())
print(getExponent(n, p))
