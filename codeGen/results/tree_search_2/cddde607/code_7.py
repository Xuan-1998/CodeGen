def countPaths(N, K, arr):
    memo = [[0] * (K + 1) for _ in range(N)]
    
    for i in range(N):
        memo[i][0] = 1
    
    for k in range(1, K + 1):
        for i in range(N):
            if i == N - 1:
                memo[i][k] = sum(arr[j][N - 1] <= k for j in range(i + 1))
            else:
                memo[i][k] = memo[i + 1][k - arr[i][i]] + memo[i][k - arr[i][i]]
    
    return memo[0][K]
