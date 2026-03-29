import sys

t, l, r = map(int, sys.stdin.readline().split())

result = 0
for i in range(t):
    if l <= r:
        result += f(l + i) * (l + i - l)
    else:
        result += f(r) * (r - l)

print(result % (10**9 + 7))
