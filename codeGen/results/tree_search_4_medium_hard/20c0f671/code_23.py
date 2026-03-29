def min_height_of_bookcase():
    n, max_shelf_width = map(int, input().split())
    books = []
    for _ in range(n):
        thickness, height = map(int, input().split())
        books.append((thickness, height))

    dp = [[[0] * (max_shelf_width + 1) for _ in range(max_shelf_width + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, max_shelf_width + 1):
            for k in range(min(i, max_shelf_width)):
                if books[i-1][0] / j <= k:
                    dp[i][j][k] = min(dp[i-1][j][min(k-1, books[i-1][0]/j)], dp[i-1][j-books[i-1][0], min(k, books[i-1][0])])
                else:
                    dp[i][j][k] = dp[i-1][j][k]

    return dp[n][max_shelf_width][-1]
