import sys
from collections import defaultdict

def solve():
    n = int(sys.stdin.readline())
    a = [0] + list(map(int, sys.stdin.readline().split()))
    dp = [-1] * (n+1)
    visited = [0] * (n+1)
    cycle = [0] * (n+1)
    
    def dfs(x):
        if x <= 0 or x > n:
            return 0
        if cycle[x]:
            return -1
        if visited[x]:
            cycle[x] = 1
            return -1
        visited[x] = 1
        dp[x] = a[x] + dfs(x + a[x])
        visited[x] = 0
        cycle[x] = 1
        return dp[x]
    
    for i in range(1, n+1):
        if dp[i] == -1:
            dfs(i)
    
    for i in range(1, n+1):
        print(dp[i])

solve()

