import sys

t, l, r = map(int, input().split())
result = 0

for i in range(t):
    result += (i * f(l + i)) % (10**9 + 7)

print(result)
