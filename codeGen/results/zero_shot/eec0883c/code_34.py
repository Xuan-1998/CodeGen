n = int(input())
w = list(map(int, input().split()))
dp = [[0]*100000 for _ in range(n)]

for i in range(1, n):
    u, v, c = map(int, input().split())
    dp[v][min(w[u-1], dp[u][c])] = max(dp[v][min(w[u-1], dp[u][c])], dp[u][c] - c)

print(max(dp[-1]))
