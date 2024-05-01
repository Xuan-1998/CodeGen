import sys

def min_falling_path_sum(A):
    R, C = len(A), len(A[0])
    dp = [[0]*C for _ in range(R)]
    
    # Initialize the first row of the DP table
    dp[0] = [x for x in A[0]]
    
    for i in range(1, R):
        for j in range(C):
            if j == 0:
                dp[i][j] = min(dp[i-1][k+1]*A[i][k] for k in range(j)) + A[i][j]
            elif j == C-1:
                dp[i][j] = min(dp[i-1][k+1]*A[i][k] for k in range(C-2, j, -1)) + A[i][j]
            else:
                dp[i][j] = min(min(dp[i-1][k+1]*A[i][k] for k in range(j-1, -1, -1)), 
                                min(dp[i-1][k+1]*A[i][k] for k in range(j+1, C))) + A[i][j]
    
    return min(dp[-1])
