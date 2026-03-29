import sys

def solve():
    n = int(sys.stdin.readline().strip())
    portals = list(map(int, sys.stdin.readline().split()))
    
    # Initialize dp array with infinite values
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(n):
        dp[portals[i]] = min(dp[portals[i]], dp[i] + 1)
    
    return dp[-1]

print(solve())
