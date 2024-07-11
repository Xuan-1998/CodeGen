n = int(input())
a = [0] + list(map(int, input().split()))
dp = [-1]*(n+1)
visited = [False]*(n+1)

def solve(i):
    if i <= 0 or i > n:
        return 0
    if visited[i]:
        return -1
    if dp[i] != -1:
        return dp[i]
    visited[i] = True
    y = a[i]
    x = i + a[i]
    res = solve(x)
    if res == -1:
        dp[i] = -1
    else:
        y += res
        dp[i] = y
    return dp[i]

for i in range(1, n+1):
    print(solve(i))

