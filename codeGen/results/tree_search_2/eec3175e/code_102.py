def can_sum_divisible_by_m(n, m):
    dp = [[False] * m for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True

    for i in range(1, n+1):
        for j in range(m):
            if j >= 0:
                dp[i][j] = dp[i-1][j] or (dp[i-1][j] and (i*(i-1)//2 + j) % m == 0)
            else:
                dp[i][j] = False

    return any(dp[n][j] for j in range(m))

n, m = map(int, input().split())
print(can_sum_divisible_by_m(n, m))
