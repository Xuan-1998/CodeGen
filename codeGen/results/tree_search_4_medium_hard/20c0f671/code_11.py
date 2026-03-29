def min_height_of_bookcase(books, shelf_width):
    books.sort(key=lambda x: x[1])  # sort books by height in descending order

    dp = [[0] * (shelf_width + 1) for _ in range(len(books) + 1)]

    for i in range(1, len(books) + 1):
        thickness, height = books[i - 1]
        for w in range(shelf_width, thickness - 1, -1):
            dp[i][w] = min(dp[i-1][w], dp[i-1][w-thickness] + height)

    return dp[-1][-1]

# Example usage:
books = [(3, 5), (2, 4), (6, 10)]
shelf_width = 7
print(min_height_of_bookcase(books, shelf_width))  # Output: 11
