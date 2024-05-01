def find_divisible_subset(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        total_sum = sum(range(i + 1))
        if total_sum % m == 0:
            dp[i][total_sum % m] = 1
        for j in range(m, -1, -1):
            if j >= total_sum % m and (dp[i - 1][j] or (i > 1 and dp[i - 1][j - (total_sum % m)])):
                dp[i][j] = 1
    
    return 1 if any(dp[n][i]) else 0

n, m = map(int, input().split())
print(find_divisible_subset(n, m))
