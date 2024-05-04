===BEGIN CODE===
import sys

# Read input
books = []
for _ in range(int(input())):
    thickness, height = map(int, input().split())
    books.append((thickness, height))

shelf_width = int(input())

# Initialize dp table
dp = [[float('inf')] * (shelf_width + 1) for _ in range(len(books) + 1)]

# Base case: no books
dp[0][0] = 0

for i in range(1, len(books) + 1):
    thickness, height = books[i-1]
    for w in range(shelf_width + 1):
        # Place book on a new shelf
        dp[i][w] = min(dp[i-1][0] + height, dp[i-1][w])
        # Try to place book on an existing shelf
        if w >= thickness:
            dp[i][w] = min(dp[i][w], dp[i-1][max(0, w-thickness)] + height)

# Return the minimum height of the bookcase for the maximum shelf width
print(min(dp[-1]))
