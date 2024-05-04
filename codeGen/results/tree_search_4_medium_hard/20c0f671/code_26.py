from sys import stdin

def min_bookcase_height():
    n, max_shelf_width = map(int, stdin.readline().split())
    books = []
    for _ in range(n):
        thickness, height = map(int, stdin.readline().split())
        books.append((thickness, height))

    dp = [[float('inf')] * (max_shelf_width + 1) for _ in range(len(books) + 1)]
    shelf_height = 0

    for i in range(len(books)):
        for j in range(max_shelf_width + 1):
            dp[i+1][j] = min(dp[i+1][j], dp[i][min(j, books[i][0])] + books[i][1])

    return min(dp[-1])

print(min_bookcase_height())
