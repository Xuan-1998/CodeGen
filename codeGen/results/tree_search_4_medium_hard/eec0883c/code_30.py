from sys import stdin

n = int(stdin.readline())
w = list(map(int, stdin.readline().split()))
parent = [-1] * (n - 1)
road_length = []

for i in range(n - 1):
    u, v, c = map(int, stdin.readline().split())
    parent[v - 1] = u
    road_length.append(c)

dp = [0] * n

for u in range(n):
    if parent[u] == -1:  # city u is the root
        dp[u] = w[u]
    else:
        parent_city = parent[u]
        dp[u] = max(dp[u], min(dp[parent_city] - road_length[u-1], w[u]))

print(max(dp))
