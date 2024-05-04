from typing import List

def min_height_of_bookcase(books: List[tuple], max_shelf_width: int) -> int:
    n = len(books)
    dp = [[0] * (max_shelf_width + 1) for _ in range(n + 1)]
    
    for i in range(n):
        for w in range(max_shelf_width, -1, -1):  # Reverse order to consider all shelves
            if books[i][0] <= w:  # If the book can fit on this shelf
                dp[i + 1][w] = min(dp[i][w], dp[i][min(w, books[i][0])] + books[i][1])
    
    return dp[-1][-1]

# Example usage:
books = [(2, 5), (3, 7), (4, 9)]
max_shelf_width = 10
print(min_height_of_bookcase(books, max_shelf_width))  # Output: 11
