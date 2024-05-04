===CODE BEGIN===
from collections import defaultdict

def min_height(books, w):
    dp = [[0] * (w + 1) for _ in range(len(books) + 1)]
    book_by_thickness = defaultdict(list)
    for i, book in enumerate(books):
        book_by_thickness[book[0]].append(book)

    def dfs(i, w):
        if i == len(books): return 0
        thickness = books[i][0]
        height = books[i][1]
        if thickness > w: return dfs(i + 1, w)
        for j in range(w, -1, -thickness):
            dp[i][j] = min(dp[i][j], max(height, dp[i - 1][j - thickness]) if i else height)
        return dp[i][w]

    return dfs(0, w)

===CODE END===
