import sys

t, l, r = map(int, input().split())

result = 0
for i in range(t):
    result += (10**i) * min(l + i, r)

print(result % (10**9 + 7))
