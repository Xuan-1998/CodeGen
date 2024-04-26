def getExponent(n, p):
    x = 0
    while n % (p ** (x + 1)) == 0:
        x += 1
    return x

n, p = map(int, input().split())
print(getExponent(n, p))
