import sys

def solve(n, w, roads):
    dp = [[0] * (10**9 + 1) for _ in range(n)]
    for i in range(n):
        dp[i][w[i]] = w[i]
    
    for u, v, c in roads:
        for j in range(10**9, -1, -c):
            if j >= c:
                dp[v][j] = max(dp[v][j], dp[u][j-c])
    
    return dp[n-1].index(max(dp[n-1]))

n = int(input())
w = list(map(int, input().split()))
roads = []
for _ in range(n-1):
    u, v, c = map(int, input().split())
    roads.append((u, v, c))

print(solve(n, w, roads))
