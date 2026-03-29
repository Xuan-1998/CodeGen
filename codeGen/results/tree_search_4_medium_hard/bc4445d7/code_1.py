import sys; input = lambda: sys.stdin.readline().strip()
n = int(input())
edges = [list(map(int, input().split())) for _ in range(n-1)]
m, k = map(int, input().split()); p = list(map(int, input().split()))
dp = [[0] * (n-1) for _ in range(n)]

for i, (u, v) in enumerate(edges):
    if u == 0 or v == 0:
        dp[u][v] = 1
    elif k % p[i] == 0 and (p[i]-1) * (k//p[i]) // ((p[i]-1)*p[i]):
        dp[u][v] = min(dp[u][v], dp[u-1][v-1] + p[i])
    else:
        dp[u][v] = dp[u-1][v-1] + 1

print(sum(sum(row) for row in dp) % (10**9+7))
