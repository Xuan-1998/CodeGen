MOD = 1000000007

def solve():
    n = int(input())
    portals = [int(x) for x in input().split()]
    
    dp = [[0] * (n + 2) for _ in range(n + 1)]
    dp[0][1] = 1
    
    for i in range(1, n + 1):
        for p_i in range(1, i + 1):
            if not (i % 2):  # ceiling has no crosses
                dp[i][p_i] = dp[i-1][p_i-1]
            else:  # ceiling has an odd number of crosses
                dp[i][p_i] = dp[i-1][portals[i-1]]
    
    return dp[n][n+1]

print(solve())
