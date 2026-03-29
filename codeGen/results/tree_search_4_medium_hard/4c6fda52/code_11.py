def min_changes(s, k):
    n = len(s)
    c = max(0, k-1)
    dp = [[float('inf')] * (c+1) for _ in range(n)]
    
    target = 'RGB'[k%3]  # determine the target character
    
    for i in range(k-1, -1, -1):
        for c in range(min(c+1, k), -1, -1):
            if i+k <= n:
                j = max(0, i-k)
                dp[i][c] = min(dp[j][c-1] + (s[i] != target) for j in range(j, i))
            else:
                break
        c -= 1
    
    return dp[0][c]
