import sys

def getExponent(n, p):
    queue = [n]
    exponents = []

    while queue:
        n = queue.pop(0)
        x = 0
        while pow(p, x) <= n:
            if n % (pow(p, x)) == 0:
                exponents.append(x)
                break
            x += 1

    return max(exponents)

n, p = map(int, input().split())
print(getExponent(n, p))
