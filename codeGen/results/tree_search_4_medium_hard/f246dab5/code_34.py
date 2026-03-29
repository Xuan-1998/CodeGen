import sys

n = int(sys.stdin.readline())
dp = [[0] * (1000001) for _ in range(4)]

for i in range(n):
    t_i = int(sys.stdin.readline())
    
    # Fill up the dp table
    for j in range(t_i, 0, -1):
        dp[3][j] = min(dp[3][j], dp[2][j-90] + 50)
        dp[2][j] = min(dp[2][j], dp[1][j-120] + 120)
        dp[1][j] = min(dp[1][j], dp[0][j-1] + 20)
    
    # Print the minimum cost for the current trip
    print(min(dp[3][t_i:]))

