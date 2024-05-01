import sys

n = int(input())
a = list(map(int, input().split()))

dp = [0] * (n + 1)
d = {}

for i in range(n):
    if i == 0:
        aj = a[i]
    else:
        aj = next((k for k in d if d[k] != aj), None)
        dp[i] = max(dp[i], dp[i - 1] + (aj - 1))
        d[i] = aj

print(dp[-1])
