def min_height(n, books, max_width):
    dp = [[[float('inf')] for _ in range(max_width + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(max_width, -1, -1):
            if books[i-1][0] <= w:
                dp[i][w][books[i-1][1]] = min(dp[i][w][books[i-1][1]], 
                                                 [dp[i-1][w-books[i-1][0]][h] for h in range(books[i-1][1], -1, -1) if h <= max_width])
                dp[i][w][min_height(i)] = min(dp[i][w][min_height(i)], 
                                               [dp[i-1][w'][h'] + books[i-1][1] for w' in range(w-books[i-1][0], -1, -1) if w' <= max_width and h' <= max_height])

    return min(dp[n][max_width])
