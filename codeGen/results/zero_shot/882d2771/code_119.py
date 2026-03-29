import sys

t, l, r = map(int, input().split())
mod = 10**9 + 7

f = lambda n: n - 1
result = 0

for i in range(t):
    if i == 0:
        result += f(l)
    else:
        result += (r - l + 1) * f(r) - f(l)

print(result % mod)
