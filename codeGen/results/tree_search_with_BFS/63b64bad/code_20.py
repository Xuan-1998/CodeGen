import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split()))
dp = [[-2 for _ in range(n+1)] for _ in range(n+1)]
visited = [[0 for _ in range(n+1)] for _ in range(n+1)]

def dfs(i, x):
    if x <= 0 or x > n:
        return 0
    if visited[i][x]:
        if dp[i][x] == -2:
            return -1
        return dp[i][x]
    visited[i][x] = 1
    dp[i][x] = -1
    y = dfs(i+a[x], x+a[x])
    if y == -1:
        return -1
    dp[i][x] = a[x] + y
    return dp[i][x]

for i in range(1, n+1):
    print(dfs(i, 1))

