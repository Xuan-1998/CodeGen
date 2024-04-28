def can_sum_divisible(m):
    n = int(input())
    x = list(map(int, input().split()))
    
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = True
            elif j == 0:
                dp[i][j] = True
            else:
                dp[i][j] = dp[i-1][j] or (j <= x[i-1] and dp[i-1][j-x[i-1]])
    
    return int(any(dp[n][:]))  # Return 1 if there's a subset, 0 otherwise

print(can_sum_divisible(int(input())))
