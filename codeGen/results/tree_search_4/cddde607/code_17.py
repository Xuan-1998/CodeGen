def numPaths(arr, N, K):
    dp = [[0 for _ in range(K+1)] for _ in range(N)]
    
    # Base case: one path from top left to itself
    dp[0][0] = 1
    
    for i in range(N):
        for j in range(K+1):
            if i > 0 and j > 0:
                if arr[i-1][j-1] <= j:
                    dp[i][j] += dp[i-1][j-1]
                if arr[i-1][j] <= j:
                    dp[i][j] += dp[i-1][j]
            else:
                if i == 0 and j > 0:
                    for k in range(j+1):
                        if arr[i][k] <= j:
                            dp[i][j] += dp[0][k]
                elif j == 0:
                    for k in range(i+1):
                        if arr[k][j] <= j:
                            dp[i][j] += dp[k][0]
    
    return dp[N-1][K]

# Example usage
N = int(input())
K = int(input())
arr = [[int(x) for x in input().split()] for _ in range(N)]

print(numPaths(arr, N, K))
