def min_squares(n, m):
    dp = [[0] * (n*m-1) for _ in range(n*m-1)]
    
    for i in range(n*m-1):
        for j in range(i+1):
            if i==j:  # base case: single cell
                dp[i][j] = 1
            else:
                min_squares = float('inf')
                for k in range(1, min(i, j)+1):  # try all possible square sizes
                    if (i-k+1)*(j-k+1) > 0:  # check if the remaining cells can be tiled
                        min_squares = min(min_squares, dp[i-k][j-k] + 1)
                dp[i][j] = min_squares
    
    return dp[-1][-1]

n, m = map(int, input().split())
print(min_squares(n, m))
