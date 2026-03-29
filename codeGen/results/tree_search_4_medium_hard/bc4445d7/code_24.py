import sys

# Read input and calculate prime factors of k
n = int(input())
edges = []
for _ in range(n-1):
    u, v = map(int, input().split())
    edges.append((u, v))

m = int(input())
prime_factors = list(map(int, input().split()))

k = 1
for p in prime_factors:
    k *= p

# Initialize DP table with size (n, n)
dp = [[0] * (n+1) for _ in range(n+1)]

# Fill up DP table in bottom-to-top manner
for u, v in edges:
    dp[u][v] = 1
    for i in range(u-1, -1, -1):
        if dp[i][u]:
            dp[i][v] = min(dp[i][v], dp[i][u])
    for i in range(v+1, n+1):
        if dp[v][i]:
            dp[v][i] = min(dp[v][i], dp[v][u])

# Calculate sum(f(i, j)) over all i <= j pairs
max_distribution_index = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        max_distribution_index += dp[i-1][j-1]

print(max_distribution_index % (10**9 + 7))
