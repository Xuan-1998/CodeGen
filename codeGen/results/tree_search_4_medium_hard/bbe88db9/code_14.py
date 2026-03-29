def min_portal_moves():
    n = int(input())
    portals = [int(x) for x in input().split()]
    
    dp = {(1, False): 0}  # Initialize with the start state
    
    for i in range(2, n+2):
        visited = (i, False)
        not_visited = (i, True)
        
        if (i-1, False) in dp:
            dp[visited] = dp[(i-1, False)] + 1
        elif (i-1, True) in dp:
            dp[visited] = dp[(i-1, True)]
        
        if (portals[i-2], False) in dp:
            dp[not_visited] = min(dp[not_visited], dp[(portals[i-2], False)] + 1)
        elif (portals[i-2], True) in dp:
            dp[not_visited] = min(dp[not_visited], dp[(portals[i-2], True)])
        
    return dp.get((n+1, False), -1)

print(min_portal_moves())
