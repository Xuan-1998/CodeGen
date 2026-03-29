import sys

n = int(input())
edges = []
for _ in range(n-1):
    u, v = map(int, input().split())
    edges.append((u, v))

m = int(input())
prime_factors = list(map(int, input().split()))

dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][i] = 0

for j in range(i+1, n+1):
    for k in range(i+1, j+1):
        dp[i][j] = min(dp[i][k-1] + 1 if k == i else dp[k-1][j], dp[k][j])

max_distribution_index = dp[1][n-1]
print(max_distribution_index % (10**9+7))
