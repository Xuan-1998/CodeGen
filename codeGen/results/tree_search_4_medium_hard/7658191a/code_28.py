def max_score(n, k, z, arr):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if j == 0:
                # No moves performed
                dp[i][j] = max(dp[i - 1][j], arr[i - 1])
            else:
                # Perform a move (either to the right or left)
                dp[i][j] = max(
                    dp[i - 1][j - 1] + arr[i - 1],
                    dp[max(i - z, 0)][j - 1] + arr[i - 1]
                )

    return dp[n][k]

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_score(n, k, z, arr))
