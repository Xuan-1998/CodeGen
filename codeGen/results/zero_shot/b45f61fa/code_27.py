import sys
from math import inf

n = int(sys.stdin.readline().strip())
p = list(map(int, sys.stdin.readline().strip().split()))

dp = [[0] * len(p) for _ in range(len(p))]

for gap in range(2):
    for i in range(len(p) - gap - 1):
        j = i + gap
        dp[i][j] = inf
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j]
            dp[i][j] = min(dp[i][j], cost)

s = []
i, j = 0, len(p) - 1
while i < j:
    k = dp[i][j].index(min(dp[i][j]))
    s.append(f"({p[i]}*{p[k+1]})")
    i, j = k + 1, j - 1

s.append(f"{p[-1]}")

print(' '.join(s))
