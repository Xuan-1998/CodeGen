def getExponent(n, p):
    x = 0
    while n % p == 0:
        n //= p
        x += 1
    return x

n, p = map(int, input().split())
print(getExponent(n, p))
