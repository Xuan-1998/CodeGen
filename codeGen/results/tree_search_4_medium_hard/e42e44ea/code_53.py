import heapq

def minInitialPoints(grid):
    N, M = len(grid), len(grid[0])
    dp = [[float('inf')] * M for _ in range(N)]
    pq = [(0, 0)]  # priority queue with initial points and cell indices
    
    while pq:
        points, i, j = heapq.heappop(pq)
        
        if i > 0 and j > 0:  # only update DP state if we can move down or right
            dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])
        
        elif i == 0:  # base case for top row
            dp[i][j] = grid[i][j]
        
        elif j == 0:  # base case for left column
            dp[i][j] = grid[i][j]
        
        if i < N - 1 and j < M - 1:
            heapq.heappush(pq, (dp[i][j] + grid[i+1][j], i+1, j))
            heapq.heappush(pq, (dp[i][j] + grid[i][j+1], i, j+1))
    
    return dp[-1][-1]  # return the minimum points required to reach the bottom-right cell

# example usage:
N = int(input())
M = int(input())
grid = [[int(x) for x in input().split()] for _ in range(N)]
print(minInitialPoints(grid))
