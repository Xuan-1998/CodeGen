import sys

# Read input
n, m = map(int, input().split())
books = []
for _ in range(n):
    thickness, height = map(int, input().split())
    books.append((thickness, height))

# Initialize dp table and max_width
dp = [[0] * (m + 1) for _ in range(n + 1)]
max_width = [0] * (n + 1)

# Fill up the table
for i in range(1, n + 1):
    for k in range(m + 1):
        if books[i - 1][0] <= k:
            dp[i][k] = max(dp[i - 1][k], height) if not dp[i - 1][k] else dp[i - 1][k]
            max_width[i] = max(max_width[i], k)
        else:
            dp[i][k] = dp[i - 1][k]

# Print the answer
print(dp[-1][-1])
