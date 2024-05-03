import sys
from collections import defaultdict

n, m = map(int, input().split())
plants = sorted([[int(s), float(x)] for s, x in (map(lambda x: list(map(int, x.split())), [input() for _ in range(n)]))], key=lambda x: x[1])

dp = defaultdict(list)
for j in range(1, m+1):
    dp[0][j] = 0

for i in range(1, n+1):
    for k in range(1, m+1):
        if plants[i-1][0] == k:
            dp[i][k] = (plants[i-1][1] - plants[i-2][1]) / (k - k) + dp[i-1][k]
        else:
            dp[i][k] = dp[i-1][k]

result = sum(dp[n][j] for j in range(1, m+1))

print(result)
