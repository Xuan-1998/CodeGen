import sys
from sys import stdin, stdout

def dfs(i, a, dp, visited):
    if i <= 0 or i > n:
        return 0
    if visited[i]:
        if dp[i] != -1:
            return dp[i]
        else:
            return -1
    visited[i] = True
    dp[i] = dfs(i + a[i], a, dp, visited)
    if dp[i] == -1:
        return -1
    dp[i] += a[i]
    return dp[i]

def solve():
    n = int(stdin.readline())
    a = [0] + list(map(int, stdin.readline().split()))
    dp = [-1]*(n+1)
    visited = [False]*(n+1)
    for i in range(1, n+1):
        stdout.write(str(dfs(i, a, dp, visited)) + "\n")

solve()

