def min_falling_path_sum(A):
    n = len(A)
    dp = [[0] * (n) for _ in range(n)]

    # Initialize the first row
    dp[0][j] = A[0][j]
    
    for i in range(1, n):
        for j in range(n):
            if i == 1:
                dp[i][j] = min(dp[i-1][k-1]*A[i][k] for k in range(j+1)) + A[i][j]
            else:
                dp[i][j] = min(dp[i-1][k-1]*A[i][k] for k in range(min(i, j)+1)) + A[i][j]
    
    return min(dp[n-1])
