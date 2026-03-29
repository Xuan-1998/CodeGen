import sys
from sys import stdin, stdout

def solve(i, a, dp, visited):
    if dp[i] != -1:
        return dp[i]
    if visited[i]:
        return -1
    visited[i] = True
    next_pos = i + a[i]
    if next_pos <= n:
        dp[i] = solve(next_pos, a, dp, visited)
        if dp[i] != -1:
            dp[i] += 2 * a[i]
    next_pos = i - a[i]
    if dp[i] == -1 and next_pos > 0:
        dp[i] = solve(next_pos, a, dp, visited)
        if dp[i] != -1:
            dp[i] += 2 * a[i]
    if dp[i] == -1:
        dp[i] = 0
    visited[i] = False
    return dp[i]

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [-1] * (n + 1)
visited = [False] * (n + 1)

for i in range(2, n + 1):
    stdout.write(str(solve(i, a, dp, visited)) + '\n')

