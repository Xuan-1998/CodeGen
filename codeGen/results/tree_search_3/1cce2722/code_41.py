===BEGIN CODE===
def solve():
    n = int(input())
    sequence = list(map(int, input().split()))
    dp = [[0] * (n // 2 + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for k in range(min(i, n // 2) + 1):
            if sequence[i - 1] == sequence[i - 2]:
                dp[i][k] = max(dp[i - 1][k], dp[i - 2][k - 1])
            else:
                dp[i][k] = max(dp[i - 1][k], dp[i - 1][k])

    return dp[n][n // 2]

print(solve())
===END CODE===
