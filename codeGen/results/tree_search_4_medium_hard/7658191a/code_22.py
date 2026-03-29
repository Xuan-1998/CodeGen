def max_score():
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    
    dp = [[-float('inf')] * (k + 1) for _ in range(n + 1)]
    for j in range(k + 1):
        dp[0][j] = 0
    
    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if i == 1 or j == 0:
                dp[i][j] = arr[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + arr[i])
    
    return dp[n][k]

print(max_score())
