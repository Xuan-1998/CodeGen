def count_ways(n, p):
    dp = [[0] * (n + 2) for _ in range(n + 1)]
    
    # base case: there's only one way to start the maze
    dp[1][0] = 1
    
    for i in range(2, n + 1):
        if p[i - 1] % 2 == 0:  # ceiling contains even crosses
            dp[i][0] = dp[p[i - 1] - 1][0]
        else:
            dp[i][0] = dp[p[i - 1]][0]
        
        for j in range(1, i + 1):
            if j < p[i - 1]:
                dp[i][j] = dp[i - 1][p[i - 2] - 1]
            elif j == p[i - 1]:
                dp[i][j] = dp[i - 1][0]
    
    return dp[n][n + 1]

# Read input from stdin
n = int(input())
p = [int(x) for x in input().split()]

print(count_ways(n, p))
