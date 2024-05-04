def minHeightShelves(books, shelfWidth):
    n = len(books)
    dp = [[[0 for _ in range(shelfWidth+1)] for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for w in range(1, min(i+1, shelfWidth)+1):
            if books[i-1][0] > w:
                dp[i][w] = dp[i-1][w]
            else:
                max_height = 0
                for j in range(i):
                    if books[j][0] <= w and books[j][1] > max_height:
                        max_height = books[j][1]
                dp[i][w] = min(dp[i-1][w], dp[i-1][w-books[i-1][0]] + max_height)
    
    return dp[n][shelfWidth]
