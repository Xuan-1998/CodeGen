import sys

t, l, r = map(int, input().split())

def f(n):
    # Implement your calculation for f(n) here
    pass

result = t * f(l)
for i in range(1, r - l + 1):
    result += t * (l + i) * f(l + i)

print(result % (10**9 + 7))
