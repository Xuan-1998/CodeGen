import sys
from math import inf

input_values = list(map(int, input().split()))
n, m = input_values[0], input_values[1]

dp = [[inf for _ in range(m+1)] for _ in range(n+1)]

for j in range(m+1):
    dp[0][j] = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        min_val = inf
        for k in range(i):
            if (k*(k+1) <= j and k >= j - i):
                min_val = min(min_val, dp[k][j-k-1] + 1)
        dp[i][j] = min_val

print(dp[n-1][m-1])
