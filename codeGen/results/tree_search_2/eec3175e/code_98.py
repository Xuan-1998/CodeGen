def find_subset_sum_divisible_by_m(x, m):
    n = len(x)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i-1][j]
            if j >= x[i-1]:
                dp[i][j] = (dp[i][j] or dp[i-1][j-x[i-1]])

    return dp[n][m]

n, m = map(int, input().split())
x = list(map(int, input().split()))
print(find_subset_sum_divisible_by_m(x, m))
