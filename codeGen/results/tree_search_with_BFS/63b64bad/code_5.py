python
n = int(input().strip())
a = [0] + list(map(int, input().strip().split()))

dp = [-1] * (n + 1)
visited = [False] * (n + 1)
calculated = [False] * (n + 1)

def solve(x):
    if x <= 0 or x > n:
        return 0
    if visited[x]:
        return -1
    if calculated[x]:
        return dp[x]
    visited[x] = True
    dp[x] = solve(x + a[x])
    if dp[x] != -1:
        dp[x] += a[x]
    visited[x] = False
    calculated[x] = True
    return dp[x]

for i in range(2, n + 1):
    print(solve(i))

