===BEGIN CODE===
import sys
from math import comb

n, m, h = map(int, input().split())
s = list(map(int, input().split()))

dp = [[0.0 for _ in range(n+1)] for _ in range(m+1)]

for i in range(1, m+1):
    dp[i][0] = sum(s[:i]) / n
for j in range(1, min(h, sum(s)) + 1):
    for i in range(j+1, m+1):
        dp[i][j] = (dp[i-1][max(0, j-1)] * comb(sum(s[:i]), j) / comb(n, j) +
                    (1 - dp[i-1][max(0, j-1)]) * dp[i-1][j])
ans = sum(dp[m][k] for k in range(1, min(n, sum(s)) + 1))
print(ans)
===END CODE===
