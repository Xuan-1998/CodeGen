def numPathsWithKCoins(K, N, arr):
    dp = [[0]*N for _ in range(N)]
    
    def dfs(i, j, k):
        if i == 0 and j == 0:
            return 1 if arr[0][0] <= k else 0
        
        if dp[i][j]:
            return dp[i][j]
        
        dp[i][j] = 0
        if arr[i][j] <= k:
            if i < N-1 and j < N-1:
                dp[i][j] += dfs(i+1, j, k-arr[i][j]) + dfs(i, j+1, k-arr[i][j])
        
        return dp[i][j]
    
    return dfs(N-1, N-1, K)

K = int(input())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(numPathsWithKCoins(K, N, arr))
