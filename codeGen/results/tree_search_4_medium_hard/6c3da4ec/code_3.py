def maxOr(s):
    n = len(s)
    
    # Edge cases: handle small inputs directly
    if n <= 1:
        return '0'
    
    dp = [[0] * (n+1) for _ in range(n)]
    
    # Base case: fill the first row of the DP table
    for j in range(n+1):
        dp[0][j] = s[:j]
    
    # Fill the DP table iteratively
    for i in range(1, n):
        for j in range(i+1, n+1):
            for k in range(i):
                dp[i][j] = max(dp[i][j], int(dp[k][i], 2) | int(dp[i][j-1], 2))
    
    # Find the maximum bitwise OR value without leading zeroes
    result = '0'
    for i in range(n+1):
        for j in range(i, n+1):
            if dp[i][j] > 0 and bin(int(dp[i][j], 2)).lstrip('0') != '0':
                result = max(result, dp[i][j])
    
    return bin(int(result, 2))[2:]
