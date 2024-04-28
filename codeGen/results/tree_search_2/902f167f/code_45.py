def minSquares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1:
                dp[i][j] = j
            elif j == 1:
                dp[i][j] = i
            else:
                for k in range(min(i, j), 0, -1):
                    a = (i // k) * k
                    b = (j // k) * k
                    dp[i][j] = min(dp[i][j], dp[a][b] + (i - a) + (j - b))
    
    return dp[n][m]

n, m = map(int, input().split())
print(minSquares(n, m))
