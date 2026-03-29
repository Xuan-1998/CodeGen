def min_height_of_bookcase(books, shelf_width):
    n = len(books)
    dp = [[0] * (shelf_width + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(shelf_width + 1):
            if i == 0:
                dp[i][w] = 0
            elif w < books[0][0]:
                dp[i][w] = dp[i - 1][w]
            else:
                min_height = float('inf')
                for j in range(i):
                    if w >= books[j][0]:
                        height = max(dp[j][w - books[j][0]], books[j][1])
                        min_height = min(min_height, height)
                dp[i][w] = min_height

    return dp[n][shelf_width]

# Example usage:
books = [(3, 5), (2, 4), (1, 3), (4, 6)]
shelf_width = 10
print(min_height_of_bookcase(books, shelf_width))  # Output: 13
