def min_height_of_bookcase(books, shelf_width):
    # Create a 2D array to store the minimum height of the bookcase for each subproblem
    dp = [[float('inf')] * (shelf_width + 1) for _ in range(len(books) + 1)]

    # Base case: when there are no more books to place, return 0 as the minimum height
    for w in range(shelf_width + 1):
        dp[0][w] = 0

    # Recursive function: consider two options for each book
    for i in range(1, len(books) + 1):
        for w in range(shelf_width + 1):
            if books[i - 1][0] <= w:  # If the current book can fit on an existing shelf
                dp[i][w] = min(dp[i][w], dp[i - 1][w - books[i - 1][0]] + books[i - 1][1])
            else:  # If the current book needs a new shelf
                dp[i][w] = min(dp[i][w], dp[i - 1][shelf_width] + books[i - 1][1])

    # Find the minimum height that is greater than or equal to the height of the tallest book
    min_height = float('inf')
    for w in range(shelf_width + 1):
        if dp[-1][w] >= max(books, key=lambda x: x[1])[1]:
            min_height = dp[-1][w]
            break

    return min_height


# Example usage:
books = [(2, 3), (4, 5), (6, 7)]
shelf_width = 10
print(min_height_of_bookcase(books, shelf_width))  # Output: 15
