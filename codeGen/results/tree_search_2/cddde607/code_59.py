def count_paths(K, N, arr):
    dp = [[False] * N for _ in range(N)]
    
    def dfs(i, j, k):
        if i == N - 1 and j == N - 1:
            return k == K
        if dp[i][j]:
            return False
        
        dp[i][j] = True
        ways = 0
        for di in [-1, 0]:
            ni = i + di
            for dj in [0, -1]:
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    k += arr[ni][nj]
                    ways += dfs(ni, nj, k)
        dp[i][j] = False
        return ways
    
    return dfs(0, 0, 0)
