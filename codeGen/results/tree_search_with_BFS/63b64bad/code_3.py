python
import sys

def solve(i):
    if i <= 0 or i > n:
        return 0
    if visited[i]:
        if dp[i] == -1:
            return -1
        else:
            return dp[i]
    visited[i] = True
    dp[i] = solve(i + a[i])
    if dp[i] == -1:
        return -1
    dp[i] += a[i]
    return dp[i]

n = int(sys.stdin.readline())
a = [0] + list(map(int, sys.stdin.readline().split()))
dp = [-1] * (n + 1)
visited = [False] * (n + 1)

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    dp[i] = solve(i)
    if dp[i] != -1:
        print(dp[i])
    else:
        print(-1)

