def min_height(n, books, shelfWidth):
    dp = [[0] * (shelfWidth + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        t, h = books[i - 1]
        for w in range(shelfWidth, 0, -1):
            if w >= t:
                dp[i][w] = min(dp[i - 1][max(0, w - t)] + h, dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][shelfWidth]

n = int(input())  # number of books
books = []  # list of book thicknesses and heights
for _ in range(n):
    t, h = map(int, input().split())
    books.append((t, h))

shelfWidth = int(input())

print(min_height(n, books, shelfWidth))
