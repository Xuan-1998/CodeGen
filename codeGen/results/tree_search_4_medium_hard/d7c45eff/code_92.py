def solve(n, k):
    s = input().strip()
    dp = [[s[:i+1]] for i in range(k)]
    
    for i in range(1, n+1):
        if i <= k:
            dp[0][i] = s[:i]
        
        for j in range(min(i+1, k), 0, -1):
            if j == k:
                dp[i][j] = min(dp[i-1][j], s[i-j:i])
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])
                
    return ''.join([dp[n-1][k]])
