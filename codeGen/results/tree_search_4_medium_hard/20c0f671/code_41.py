def min_height(books, max_width):
    n = len(books)
    dp = [[0] * (max_width + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(max_width + 1):
            if books[i - 1][0] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = min(dp[i - 1][w], dp[i - 1][min(w, books[i - 1][0])]) + books[i - 1][1]
    
    return dp[n][max_width]

# Example usage
books = [(2, 3), (5, 4), (7, 6)]
max_width = 10

print(min_height(books, max_width))
