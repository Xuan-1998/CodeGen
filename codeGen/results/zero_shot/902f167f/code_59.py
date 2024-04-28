n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i < j:
            dp[i][j] = min(dp[i][k] for k in range(j)) + 1
        else:
            dp[i][j] = min(dp[i - k][j] for k in range(i)) + 1
print(min(dp[-1][-1], (n // 2) * (m // 2) + ((n % 2 and m % 2) or n % 2 == m % 2)))
