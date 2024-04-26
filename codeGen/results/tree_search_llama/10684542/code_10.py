def getExponent(n,p):
    exponent = 0
    while True:
        if pow(p,exponent) >= n:
            return exponent - 1
        exponent += 1

n = int(input())
p = int(input())

print(getExponent(n,p))
