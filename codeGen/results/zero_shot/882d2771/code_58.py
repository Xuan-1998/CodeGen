import sys

t, l, r = map(int, input().split())
result = 0
for i in range(t):
    if i % 2 == 0:
        result += f(l + i)
    else:
        result -= (l + i) * f(r - i)

print(result % (10**9 + 7))
