from collections import deque

def numPaths(arr):
    N = len(arr)
    k = int(input())
    
    # Create a 2D DP table
    dp = [[[False] * (k+1) for _ in range(N)] for _ in range(N)]
    
    # Base case: Only one path to reach the bottom right cell with K coins
    dp[-1][-1][0] = True
    
    # Fill up the DP table from bottom-right to top-left
    for i in range(N-2, -1, -1):
        for j in range(N-2, -1, -1):
            if arr[i][j] > k:
                continue
            
            # Check all possible moves from cell (i, j)
            for x, y in [(0, 1), (1, 0)]:
                ni, nj = i+x, j+y
                if 0 <= ni < N and 0 <= nj < N:
                    for coin in range(1, k+1):
                        if dp[ni][nj][coin-arr[i][j]]:
                            dp[i][j][coin] = True
    
    # Count the number of valid paths that collect exactly K coins
    count = 0
    for i in range(N):
        for j in range(N):
            if dp[i][j][k]:
                count += 1
    
    return count

# Read input from stdin
K, N = map(int, input().split())
arr = [[int(x) for x in input().split()] for _ in range(N)]

print(numPaths(arr))
