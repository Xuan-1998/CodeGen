import sys

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a+b
    return b % (10**9 + 7)

t, l, r = map(int, input().split())
result = sum(ti*f(l+i) for ti, i in enumerate(range(r-l))) - l*f(r)
print(result % (10**9 + 7))
