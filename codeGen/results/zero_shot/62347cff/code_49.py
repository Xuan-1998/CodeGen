import sys
from io import StringIO

def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0]*n for _ in range(m)]

    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[m-1][n-1]

# test your solution
input_str = """
4 3
1 2 3
5 6 9
3 7 8
0 0 0
"""

stdin = StringIO(input_str)
stdout = StringIO()
sys.stdin = stdin

print(minPathSum([[int(x) for x in line.split()] for line in stdin.readlines()]))
