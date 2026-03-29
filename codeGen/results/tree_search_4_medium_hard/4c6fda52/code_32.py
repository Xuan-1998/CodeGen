def min_changes(s):
    n = len(s)
    k = int(input())
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if s[i - 1] != 'RGB'[i % 3]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]
    
    return min(dp[k:])
