import sys

def count_paths(K, N, arr):
    dp = [[0] * N for _ in range(N)]
    
    # Initialize base cases: there's one way to reach each of the first row or column cells
    for i in range(N):
        dp[0][i] = 1 if (K == 0) else 0
        dp[i][0] = 1 if (K == 0) else 0
    
    # Fill up the table using dynamic programming
    for i in range(1, N):
        for j in range(1, N):
            # Calculate the number of ways to reach cell (i, j)
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            # If the current cell contains K coins, add 1 to the count
            if arr[i][j] == K:
                dp[i][j] += 1
    
    # Calculate the number of paths that collect exactly K coins
    return sum(dp[-1]) + sum([row[-1] for row in dp])

K = int(input())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(count_paths(K, N, arr))
