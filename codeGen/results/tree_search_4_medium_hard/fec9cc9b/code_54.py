def is_ladder(a):
    n = len(a)
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        last = 0
        for j in range(i, -1, -1):
            if a[j-1] >= a[last]:
                dp[i][j] = dp[i-1][last]+1
                last = j-1
            else:
                dp[i][j] = 0
                last = j-1
                
    for i in range(1, n+1):
        if dp[n][i] >= n-i+1:
            return "Yes"
    return "No"
