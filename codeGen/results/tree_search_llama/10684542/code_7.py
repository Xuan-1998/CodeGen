def getExponent(n, p):
    exponent = 0
    while n >= p ** (exponent + 1):
        exponent += 1
    return exponent - 1

n = int(input())
p = int(input())

print(getExponent(n, p))
