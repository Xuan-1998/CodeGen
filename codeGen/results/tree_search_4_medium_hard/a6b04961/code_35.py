import sys

def has_edge(u, v):
    # Read edges from stdin and check if there's an edge between vertices u and v
    pass

n, m = map(int, input().split())
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i, n + 1):
        if not has_edge(j - 1, j):  # Check if there's an edge between vertices
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) + (j - i)  # Update the maximum beauty
        else:
            dp[i][j] = dp[i][j - 1]

print(dp[-1][-1])
