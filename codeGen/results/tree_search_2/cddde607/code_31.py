def numPathsWithKCoins(N, arr):
    K = int(input())
    dp = [[False] * N for _ in range(N)]

    # Initialize base case
    dp[N-1][N-1] = True

    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        sum_coins = 0
        for x in range(i, N):
            for y in range(j, N):
                sum_coins += arr[x][y]
                if sum_coins == K and x == N-1 and y == N-1:
                    return True
        
        dp[i][j] = False
        memo[(i, j)] = False

        if i < N-1:
            if dfs(i+1, j):
                dp[i][j] = True
        if j < N-1:
            if dfs(i, j+1):
                dp[i][j] = True
        
        return dp[i][j]

    # Count the number of paths that collect exactly K coins
    count = 0
    for i in range(N):
        if dfs(i, 0):
            count += 1
    
    return count

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(numPathsWithKCoins(N, arr))
