import sys

def solve():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    
    dp = [0] * (n + 1)
    visited = set()
    
    for i in range(2, n + 1):
        for j in range(i - 1, -1, -1):
            if (j, i) not in edges and j not in visited:
                dp[i] = max(dp[i], dp[j] * (i + 1))
        visited.add(i)
    
    return dp[-1]

print(solve())
