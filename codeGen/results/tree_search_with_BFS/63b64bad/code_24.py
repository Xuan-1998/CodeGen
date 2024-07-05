python
import sys
from sys import stdin, stdout
input = stdin.readline

def dfs(pos):
    if pos <= 0 or pos > n:
        return 0
    if visited[pos]:
        if dp[pos] != -1:
            return dp[pos]
        else:
            return -1
    visited[pos] = True
    dp[pos] = a[pos] + dfs(pos + a[pos])
    if dp[pos] == -1:
        return -1
    dp[pos] = a[pos] + dfs(pos - a[pos])
    return dp[pos]

n = int(input())
a = [0] + list(map(int, input().split()))
dp = [-1] * (n + 1)
visited = [False] * (n + 1)
dp[1] = 0
visited[1] = True

for i in range(2, n + 1):
    stdout.write(str(dfs(i)) + '\n')

