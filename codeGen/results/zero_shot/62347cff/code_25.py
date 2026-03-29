    code block:
    import sys

    m, n = map(int, input().split())
    grid = [[int(x) for x in input().split()] for _ in range(m)]
    dp = [[0] * n for _ in range(m)]

    # Base case: Initialize the first element
    dp[0][0] = grid[0][0]
    
    # Fill up the first column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Fill up the first row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Fill up the rest of the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    # The minimum sum is stored at the bottom right corner
    print(dp[-1][-1])
