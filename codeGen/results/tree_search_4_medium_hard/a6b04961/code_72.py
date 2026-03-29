import sys

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))

# Initialize 2D table with zeros
dp = [[0] * (n + 1) for _ in range(n + 1)]

# Function to update the beauty of a hedgehog
def update_beauty(tail_length, number_of_spines):
    return tail_length * number_of_spines

# Fill up the 2D table
for i in range(1, n + 1):
    for j in range(i, n + 1):
        if i > n // 2:
            break
        for edge in edges:
            u, v = edge
            if (u < i and v >= i) or (u >= i and v < j):
                dp[i][j] = max(dp[i][j], update_beauty(i - j + 1, number_of_spines + 1))
        for k in range(j - 1, i - 1, -1):
            if dp[k][i]:
                break
        else:
            dp[j][i] = dp[i][j]

# Print the maximum possible beauty of a hedgehog
print(max(max(row) for row in dp))
