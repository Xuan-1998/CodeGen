import sys

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    
    # Initialize dp array with False values
    dp = [[False] * (k + 1) for _ in range(n)]
    
    # For leaf nodes, set their corresponding dp values as True if they meet the condition
    for i in range(1, n):
        x = values[i]
        for j in range(min(k, len(values) - i), 0, -1):
            dp[i][j] = (dp[i-1][j-1] and ((x ^ values[0]) == 0))
    
    # Check whether it's possible to delete at most k-1 edges from the entire tree
    return "YES" if dp[0][k-1] else "NO"

print(solve())
