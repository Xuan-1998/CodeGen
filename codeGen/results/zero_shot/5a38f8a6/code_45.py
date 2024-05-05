def minSquares(n):
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = i
    
    for j in range(n + 1):
        if j == 0:
            continue
        square_root = int(j ** 0.5)
        
        for i in range(1, n + 1):
            if i <= square_root * square_root:
                dp[i][j] = min(dp[i][j], dp[i - i ** 2][j - 1]) + 1
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][n]

if __name__ == "__main__":
    n = int(input())
    print(minSquares(n))
