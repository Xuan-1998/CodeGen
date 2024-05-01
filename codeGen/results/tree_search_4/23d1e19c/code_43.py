import sys

n, m = map(int, input().split())
dp = [[[0, 0] for _ in range(m+1)] for _ in range(n)]

# Initialize base case (vertices in fixed path)
for i in range(k-1):
    u, v = p[i], p[i+1]
    dp[u][0][0] = dp[v][0][0] + 1
    dp[u][0][1] = max(dp[u][0][1], dp[v][0][0] + 1)

# Dynamic programming loop
for j in range(1, m+1):
    for i in range(n):
        if i == p[j-1]:  # vertex in fixed path
            continue
        for u in range(i):  # previous vertices
            if (u, i) in edges:  # edge from u to i exists
                dp[i][j][0] = min(dp[i][j][0], dp[u][j-1][0] + 1)
                dp[i][j][1] = max(dp[i][j][1], dp[u][j-1][1] + 1)

# Output the minimum and maximum number of recomputations
print(min(max(dp)), max(max(dp)))
