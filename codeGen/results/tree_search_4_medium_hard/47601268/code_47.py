def find_count(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        if bin(i).count('1') == 1:
            dp[i] = sum(dp[j] for j in range(i))
        else:
            dp[i] = 1
    
    return dp[n]
