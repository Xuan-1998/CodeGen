python
n = int(input().strip())
a = [0] + list(map(int, input().split()))

dp = [-1] * (n+1)
visited = [False] * (n+1)

def simulate_from(i):
    if i <= 0 or i > n:
        return 0
    if visited[i]:
        if dp[i] == -1:
            return -1
        else:
            return dp[i]
    visited[i] = True
    dp[i] = a[i] + simulate_from(i + a[i])
    if dp[i] == -1:
        return -1
    dp[i] = max(dp[i], a[i] + simulate_from(i - a[i]))
    if dp[i] == -1:
        return -1
    return dp[i]

for i in range(2, n+1):
    print(simulate_from(i))

