def findPath(K, N, arr):
    memo = {}

    def dfs(i, j, k):
        if (i, j, k) in memo:
            return memo[(i, j, k)]
        
        if i == N - 1 and j == N - 1:
            return 1 if k == 0 else 0
        
        result = 0
        if i < N - 1:
            result += dfs(i + 1, j, k - arr[i][j]) if k >= arr[i][j] else 0
        if j < N - 1:
            result += dfs(i, j + 1, k - arr[i][j]) if k >= arr[i][j] else 0
        
        memo[(i, j, k)] = result
        return result

    return dfs(0, 0, K)
