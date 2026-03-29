import sys

t, l, r = map(int, sys.stdin.readline().split())
result = 0

for i in range(t):
    n = l + i
    if n == l:
        f_n = 0
    else:
        f_n = 1
    result += t[i] * f_n - l * (n > r)

print(result % (10**9 + 7))
