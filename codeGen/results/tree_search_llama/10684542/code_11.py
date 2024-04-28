def getExponent(n,p):
    exponent = 0
    while n % p == 0:
        n /= p
        exponent += 1
    return exponent

n, p = map(int, input().split())
print(getExponent(n, p))
