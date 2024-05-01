def count_paths(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    
    # Base case: Top-left corner with K coins
    dp[0][0][K] = 1
    
    for i in range(N):
        for j in range(N):
            for k in range(K + 1):
                if (i == N - 1 and j == N - 1) or arr[i][j] <= k:
                    # Consider taking a coin
                    if i < N - 1 and dp[i+1][j][k-arr[i][j]] > 0:
                        dp[i][j][k] += dp[i+1][j][k-arr[i][j]]
                    if j < N - 1 and dp[i][j+1][k-arr[i][j]] > 0:
                        dp[i][j][k] += dp[i][j+1][k-arr[i][j]]
    
    return sum([sum(row) for row in dp[-1]])

# Test your function
K = int(input())
N = int(input())
arr = [[int(x) for x in input().split()] for _ in range(N)]
print(count_paths(K, N, arr))
