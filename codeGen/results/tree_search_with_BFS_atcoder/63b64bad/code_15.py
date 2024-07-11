n = int(input())
a = [0] + list(map(int, input().split()))
dp = [-1] * (n+1)
visited = [False] * (n+1)

def simulate(i, y):
    if i <= 0 or i > n:
        return y
    if visited[i]:
        return -1
    visited[i] = True
    dp[i] = simulate(i+a[i], y+a[i])
    return dp[i]

for i in range(2, n+1):
    visited = [False] * (n+1)
    print(simulate(i, 0))

