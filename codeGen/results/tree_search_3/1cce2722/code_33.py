n = int(input())
sequence = list(map(int, input().split()))

dp = [[0] * 106 for _ in range(n + 1)]

for i in range(1, n + 1):
    for k in range(1, min(i, 105) + 1):
        if sequence[i - 1] == k:
            dp[i][k] = max(dp[i - 1][k], dp[i - 1][k - 1])
        else:
            dp[i][k] = dp[i - 1][k]

print(max(dp[n]))
