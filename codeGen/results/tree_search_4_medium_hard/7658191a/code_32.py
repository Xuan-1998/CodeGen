def max_score():
    n, k, z = map(int, input().split())
    scores = list(map(int, input().split()))
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if j <= z:
                dp[i][j] = max(dp[i - 1][j - 1] + scores[i - 1], dp[i - 2][j - 1] + scores[i - 2]) if i >= 2 else scores[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j - 1] + scores[i - 1], dp[i - 1][j - 2] + scores[i - 2]) if i >= 2 else scores[i - 1]
    
    return dp[n][k]

print(max_score())
