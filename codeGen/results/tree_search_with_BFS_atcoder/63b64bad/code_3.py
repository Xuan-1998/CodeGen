import sys
from sys import stdin, stdout

def solve(i, a, dp, visited):
    if i > n or i <= 0:
        return 0
    if visited[i]:
        return -1
    if dp[i] != -1:
        return dp[i]
    visited[i] = True
    dp[i] = a[i] + solve(i + a[i], a, dp, visited)
    visited[i] = False
    if dp[i] < 0:
        dp[i] = -1
    return dp[i]

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [-1] * (n + 1)
visited = [False] * (n + 1)

for i in range(1, n + 1):
    stdout.write(str(solve(i, a, dp, visited)) + '\n')

