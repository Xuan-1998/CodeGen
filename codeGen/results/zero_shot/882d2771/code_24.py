import sys

t, l, r = map(int, input().split())

def f(n):
    return n - 1

result = 0
for i in range(t):
    if i < l:
        result += t0 * (i - 1)
    elif i == l:
        result += t0 * l
    else:
        result -= l * (f(r) - f(i-1))

print(result % (10**9 + 7))
