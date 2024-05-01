def numPaths(arr, K, N):
    memo = [[[0 for _ in range(K+1)] for _ in range(N)] for _ in range(N)]

    def dfs(i, j, k):
        if i == N-1 and j == N-1:
            return 1 if arr[i][j] <= k else 0
        if memo[i][j][k] != 0:
            return memo[i][j][k]
        
        ans = 0
        if arr[i][j] <= k:
            ans += dfs(i+1, j, k-arr[i][j])
            ans += dfs(i, j+1, k-arr[i][j])
        memo[i][j][k] = ans
        return ans

    return dfs(0, 0, K)
