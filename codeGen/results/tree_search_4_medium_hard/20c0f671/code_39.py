def min_height(n, w):
    # Define dp[i][w] as the minimum height of the bookcase after placing the first i books, given a remaining shelf width w.
    dp = [[0 for _ in range(w + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if books[i - 1][0] <= j:
                # Calculate the maximum height of the current shelf by considering all possible placements of the current book.
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - books[i - 1][0]] + books[i - 1][1])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][w]
