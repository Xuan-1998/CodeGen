import sys

def f(n):
    if n <= 1:
        return 0
    else:
        return min(f(n // 2) + 1)

t, l, r = map(int, input().split())

print(sum(t * (f(i) for i in range(l, r+1)) % (10**9 + 7)))
