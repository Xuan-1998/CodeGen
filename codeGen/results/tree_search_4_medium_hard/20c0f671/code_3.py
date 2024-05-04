import sys

def min_height_of_bookcase():
    # Read input from stdin
    books = []
    for _ in range(int(input())):
        thickness, height = map(int, input().split())
        books.append((thickness, height))

    max_shelf_width = int(input())

    # Initialize dp table with infinity values
    dp = [[float('inf')] * (max_shelf_width + 1) for _ in range(len(books) + 1)]

    # Base case: no books on the bookcase
    dp[0][0] = 0

    # Fill up the dp table using tabulation
    for i in range(len(books)):
        for w in range(max_shelf_width, -1, -1):
            if books[i][0] <= w:
                dp[i + 1][w] = min(dp[i + 1][w], dp[i][max(w - books[i][0], 0)] + books[i][1])
            else:
                dp[i + 1][w] = float('inf')

    # Return the minimum height of the bookcase when all books are placed
    return dp[-1][-1]

print(min_height_of_bookcase())
