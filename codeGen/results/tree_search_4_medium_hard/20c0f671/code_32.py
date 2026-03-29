===BEGIN CODE===
def solve(n, w, books):
    dp = [[0] * (w + 1) for _ in range(n + 1)]
    book_heights = sorted([(h, t) for _, h, t in books])

    for i in range(1, n + 1):
        for j in range(w + 1):
            if book_heights[i - 1][1] <= j:
                dp[i][j] = min(dp[i - 1][j], book_heights[i - 1][0] + dp[i - 1][j - book_heights[i - 1][1]])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][w]

n, w = map(int, input().split())
books = []
for _ in range(n):
    h, t, wt = map(int, input().split())
    books.append((t, h, wt))

print(solve(n, w, books))
===END CODE===
