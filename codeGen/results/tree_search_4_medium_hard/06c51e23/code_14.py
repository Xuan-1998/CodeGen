def max_grade(n, t):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if i > 0:
            t -= 9
            while t >= 10 and i > 0:
                t -= 10
                i -= 1
            dp[i] = max(dp[i-1], dp[i-1] + (t < 9))
        else:
            dp[0] = 0
    
    return dp[n]
