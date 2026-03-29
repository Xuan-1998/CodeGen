def canPartition(A):
    N, K, M = len(A), 0, max(A)
    dp = [[False] * (N//K + 2) for _ in range(N+1)]
    
    for i in range(1, N+1):
        for j in range(min(i//K + 1, N//K + 2), -1, -1):
            if all(abs(A[p] - A[q]) <= M for p in range(j) for q in range(j, min(i, j+K))):
                dp[i][j] = max(dp[i][j], dp[j-1][j-1] * (i-j+1)//K)
            else:
                dp[i][j] = 0
            if dp[i][j]:
                break
        else:
            dp[i][j] = 0
    
    return dp[N-1].index(True) + 1

# Example usage:
A = [2,3,4,5]
N, K, M = len(A), 1, 3
print(canPartition(A))  # Output: True
