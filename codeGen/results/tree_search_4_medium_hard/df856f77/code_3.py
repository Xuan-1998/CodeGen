import sys

input()
n = int(input())
A = list(map(int, input().split()))

dp = [[0] * (1 << 31) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][A[i - 1]] = dp[i - 1][A[i - 1]] + 1
    for j in range(A[i - 1] - 1, -1, -1):
        dp[i][j] = min(dp[i][j], dp[i - 1][j] + (A[i] > j))

print(min(dp[n]))
