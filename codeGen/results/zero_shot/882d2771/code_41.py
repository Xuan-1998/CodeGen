import sys

t, l, r = map(int, input().split())

def f(n):
    if n <= 1:
        return 0
    res = []
    for k in range(2, n+1):
        res.append(min(f(k-1) + f(n-k)) + 1)
    return min(res)

print((t * sum([f(i) for i in range(l, r+1)])) - (l * f(r))) % (109 + 7)
