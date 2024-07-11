import sys
from sys import stdin, stdout

def solve(i):
    visited[i] = 1
    next_i = i + a[i] if i + a[i] <= n else i - a[i]
    if next_i <= 0 or next_i > n:
        dp[i] = a[i]
    elif visited[next_i] == 1 and dp[next_i] == 0:
        dp[i] = -1
    elif dp[next_i] != 0:
        dp[i] = a[i] + dp[next_i]
    else:
        dp[i] = a[i] + solve(next_i)
    visited[i] = 2
    return dp[i]

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [0] * (n + 1)
visited = [0] * (n + 1)

for i in range(1, n + 1):
    if visited[i] == 0:
        solve(i)

for i in range(1, n + 1):
    stdout.write(str(dp[i]) + '\n')

