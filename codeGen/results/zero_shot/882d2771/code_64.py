import sys

t, l, r = map(int, input().split())

def f(n):
    if n <= 2:
        return 1
    else:
        return (n // 2) * 3 + 2

result = sum(t * f(i) for i in range(l, r+1)) - l * f(r)
print(result % (10**9 + 7))
