import sys

t, l, r = map(int, input().split())

def f(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return f(n // 2) + 1
    else:
        return f((n + 1) // 2) + 1

result = 0
for i in range(t):
    result += t[i] * f(l + i)
result -= l * f(r)

print(result % (10**9 + 7))
