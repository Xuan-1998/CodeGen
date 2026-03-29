import sys
input = sys.stdin.readline

def dfs(x):
    if x <= 0 or x > n:
        return 0
    if visited[x]:
        if not done[x]:
            return -1
        return dp[x]
    visited[x] = True
    dp[x] = dfs(x + a[x])
    if dp[x] == -1:
        return -1
    dp[x] += a[x]
    done[x] = True
    return dp[x]

n = int(input())
a = [0] + list(map(int, input().split()))
visited = [False] * (n + 1)
done = [False] * (n + 1)
dp = [0] * (n + 1)

for i in range(1, n + 1):
    if not visited[i]:
        dp[i] = dfs(i)
    print(dp[i])

