def count_ones(n):
    dp = [[0]*10 for _ in range(n+1)]
    
    # Base case: single-digit numbers
    for i in range(10):
        if i == 1:
            dp[1][i] = 1
    
    for i in range(2, n+1):
        for j in range(10):
            if j < i:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][9] + (int(str(i)[j]) == 1)
    
    return sum(dp[n])
