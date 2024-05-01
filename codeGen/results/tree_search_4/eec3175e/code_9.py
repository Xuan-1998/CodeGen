def can_sum_divisible(m, arr):
    n = len(arr)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][m]


n, m = map(int, input().split())
arr = list(map(int, input().split()))

print(can_sum_divisible(m, arr))
