===BEGIN SOLUTION===
from sys import stdin, stdout

def solve():
    n = int(stdin.readline())
    grid = [list(map(int, stdin.readline().split())) for _ in range(n)]

    # Initialize memo and dp
    memo = {}
    dp = [[float('inf')] * n for _ in range(n)]
    
    def dfs(i, j):
        if (i, j) not in memo:
            if i == 0:
                dp[i][j] = grid[i][j]
                memo[(i, j)] = dp[i][j]
            else:
                dp[i][j] = min(dp[i-1][k] for k in range(j)) + grid[i][j]
                memo[(i, j)] = dp[i][j]
        return memo[(i, j)]

    # Calculate the minimum sum of a falling path with non-zero shifts
    result = float('inf')
    for j in range(n):
        result = min(result, dfs(0, j))
    stdout.write(str(result) + '\n')

if __name__ == "__main__":
    solve()
===END SOLUTION===
