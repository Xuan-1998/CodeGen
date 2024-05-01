def has_subset_sum(n, m, values):
    dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for k in range(m + 1):
            if k >= values[i - 1]:
                dp[i][k] = (k == values[i - 1] or dp[i-1][k])
            else:
                dp[i][k] = dp[i-1][k]
    
    return int(dp[n][m % m])

n, m = map(int, input().split())
values = list(map(int, input().split()))
print(has_subset_sum(n, m, values))
