import sys
from sys import stdin, stdout
sys.setrecursionlimit(10**6)

def dfs(i):
    visited[i] = True
    next_i = i + a[i]
    if next_i <= 0 or next_i > n:
        dp[i] = a[i]
    elif visited[next_i]:
        if in_cycle[next_i]:
            in_cycle[i] = True
            dp[i] = -1
        else:
            dp[i] = a[i] + dp[next_i]
    else:
        dp[i] = dfs(next_i)
        if dp[i] != -1:
            dp[i] += a[i]
        else:
            in_cycle[i] = True
    return dp[i]

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [-2] * (n+1)
visited = [False] * (n+1)
in_cycle = [False] * (n+1)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)

for i in range(1, n+1):
    stdout.write(str(dp[i]) + '\n')

