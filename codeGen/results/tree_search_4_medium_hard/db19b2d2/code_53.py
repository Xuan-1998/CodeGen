import sys
from math import comb

n, m, h = map(int, input().split())
s = list(map(int, input().split()))

dp = [[0.0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(min(i, h)+1):
        dp[i][j] = sum(s[k-1] * comb(n-k, i-k) / (comb(m, 1)) ** k for k in range(j, min(i, h)+1))

print("%.6f" % dp[n][h])
