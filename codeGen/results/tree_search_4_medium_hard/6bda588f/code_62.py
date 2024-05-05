def minF(a):
    n = len(a)
    dp = [[0] * (2*s + 1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(-s, s+1):
            if i == 1:
                dp[i][j] = a[0]
            elif i == 2:
                dp[i][j] = max(dp[i-1][j-a[0]] + a[0], dp[i-1][j])
            else:
                for x in range(min(a[0], j), -s):
                    if j-x >= 0 and (j-x) % 2 == 0:
                        dp[i][j] = min(dp[i][j], dp[i-1][x-a[0]] + a[0])
    
    return dp[n][2*s]
