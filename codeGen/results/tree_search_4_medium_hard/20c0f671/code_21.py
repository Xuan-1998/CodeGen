import sys

n, w = map(int, input().split())  # Read the number of books and the maximum shelf width
books = []  # Initialize an empty list to store book information
for _ in range(n):
    t, h = map(int, input().split())
    books.append((t, h))  # Store each book's thickness and height

dp = [[0] * (w + 1) for _ in range(n + 1)]  # Initialize the dynamic programming table
for i in range(1, n + 1):
    t, h = books[i - 1]
    for j in range(min(w, t), -1, -1):  # Iterate over shelf widths in reverse order
        if j >= t:
            dp[i][j] = min(dp[i][j], dp[i - 1][j - t] + h)
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][w])  # Print the minimum possible height of the bookcase
