import math

def f(n):
    return math.floor(math.log2(n + 1))

def solve(t, l, r):
    res = 0
    for i in range(t):
        if i == 0:
            res += f(l)
        else:
            res += f(l + i) - f(l)
    return (res - l * f(r)) % (10**9 + 7)

t, l, r = map(int, input().split())
print(solve(t, l, r))
