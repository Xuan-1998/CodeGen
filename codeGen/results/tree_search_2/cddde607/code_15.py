def count_paths(K, N, arr):
    memo = {}
    
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == N-1 and j == N-1:
            return 1 if arr[i][j] == K else 0
        
        ways = 0
        if i < N-1:  # can move down
            ways += dp(i+1, j)
        if j < N-1:  # can move right
            ways += dp(i, j+1)
        
        memo[(i, j)] = ways
        return ways
    
    return dp(0, 0)

K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(count_paths(K, N, arr))
