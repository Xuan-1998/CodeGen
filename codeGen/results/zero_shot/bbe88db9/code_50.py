import sys

def count_portal_moves(n, portals):
    dp = [0] * (n + 1)
    
    def dfs(i):
        if i >= n:
            return 1
        if dp[i]:
            return dp[i]
        
        first_portal = dfs(portals[i-1]) + 1
        second_portal = dfs(portals[i-1]) + (i % 2 == 0) * 2
        
        dp[i] = min(first_portal, second_portal)
        return dp[i]
    
    return dfs(1)

n = int(input())
portals = [int(x) for x in input().split()]
print(count_portal_moves(n, portals))
