import sys

def min_height_of_bookcase(books, max_shelf_width):
    dp = [[float('inf')] for _ in range(max_shelf_width + 1)]
    dp[0] = [0] * (max_shelf_width + 1)
    
    for book in books:
        for shelf_width in range(max_shelf_width, -1, -1):
            if book[0] <= shelf_width and dp[shelf_width][dp[shelf_width - book[0]].index(min(dp[shelf_width - book[0]]))] > dp[shelf_width - book[0]][min(dp[shelf_width - book[0]])]:
                dp[shelf_width][dp[shelf_width - book[0]].index(min(dp[shelf_width - book[0]])))] = min(min(dp[shelf_width - book[0]]), max(book[1], dp[shelf_width - book[0]][min(dp[shelf_width - book[0]])]))
    
    return min(dp[max_shelf_width])

# Example usage:
books = [(2, 4), (3, 5), (1, 3)]
max_shelf_width = 6
print(min_height_of_bookcase(books, max_shelf_width))  # Output: 7
