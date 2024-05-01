def numPathsWithKCoins(K, N, arr):
    memo = {}
    dp = [[0]*N for _ in range(N)]

    def dfs(i, j, coins):
        if i == 0 and j == 0:
            return 1 if coins == K else 0
        if (i, j, coins) in memo:
            return memo[(i, j, coins)]
        
        ways = 0
        if i > 0:
            ways += dfs(i-1, j, coins + arr[i][j])
        if j > 0:
            ways += dfs(i, j-1, coins + arr[i][j])
        
        memo[(i, j, coins)] = ways
        return ways

    return dfs(N-1, N-1, 0)
