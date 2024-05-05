import sys

n = int(input())
k_ = [int(x) for x in input().split()]
h_ = [int(x) for x in input().split()]

dp = [[0 for _ in range(max(k_) + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(min(k_), max(k_) + 1):
        if i == n:
            dp[i][j] = j
        else:
            if j >= k_[i - 1]:
                dp[i][j] = min(dp[i][j], dp[i-1][k_[i-1]] + h_[i-1])
            dp[i][j] = min(dp[i][j], dp[i][min(j, k_[i] - 1)])

print(min(dp[n]))
