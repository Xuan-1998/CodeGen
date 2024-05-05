def solve():
    n = int(input())
    portals = [int(x) for x in input().split()]
    
    dp = [[float('inf')] * 2 for _ in range(n+1)]
    dp[0][0] = 0
    
    for i in range(1, n+1):
        if not dp[i-1][0].isinf():
            dp[i][0] = min(dp[portals[i-1]][1], dp[i-1][0]) + 1
            dp[i][1] = float('inf')
            
            for j in range(i):
                if not dp[j][0].isinf() and (dp[j][1] < float('inf')):
                    dp[i][1] = min(dp[i][1], dp[j][0] + 1)
                    
    return dp[n][1]

print(solve())
