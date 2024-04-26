def getExponent(n, p):
    max_x = 0
    for x in range(0, n//p + 1):
        if n // x % p == 0:
            max_x = x
            break
    return max_x

n, p = map(int, input().split())
print(getExponent(n, p))
