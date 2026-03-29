# Read input
n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

# Sort edges by their end vertices
edges.sort()

# Initialize variables for the dynamic programming table
dp = [[0] * (n + 1) for _ in range(n + 1)]
tail_length = [0] * (n + 1)
spines = [0] * (n + 1)

# Fill up the dynamic programming table
for i in range(1, n + 1):
    for j in range(i, n + 1):
        dp[i][j] = max(dp[i - 1][k] for k in range(j)) if i > 1 else 0

# Find the maximum beauty of a hedgehog
max_beauty = 0
for i in range(1, n + 1):
    for j in range(i, n + 1):
        max_beauty = max(max_beauty, dp[i][j] * (j - i + 1))

print(max_beauty)
