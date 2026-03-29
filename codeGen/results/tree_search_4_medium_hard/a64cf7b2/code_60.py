import sys

def solve():
    n, m, T = map(int, input().split())
    
    # Initialize dp dictionary
    dp = {(i, None): 0 for i in range(1, n+1)}
    dp[1, None] = 1
    
    # Process edges
    for _ in range(m):
        u, v, t = map(int, input().split())
        
        for prev in range(n+1):
            if (prev, u) in dp and t + dp[(prev, u)] <= T:
                dp[(v, None)] = max(dp[(v, None)], dp[(prev, u)] + 1)
    
    # Return the maximum number of vertices that can be visited
    return dp[(n, None)]

print(solve())
