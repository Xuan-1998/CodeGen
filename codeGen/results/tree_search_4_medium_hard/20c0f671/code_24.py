from itertools import combinations

max_shelf_width = int(input())
books = [list(map(int, input().split())) for _ in range(int(input()))]

dp = [[float('inf')] * (max_shelf_width + 1) for _ in range(len(books) + 1)]

for i in range(1, len(books) + 1):
    for j in range(1, max_shelf_width + 1):
        dp[i][j] = float('inf')
        for k in range(i):
            if books[k][0] <= j:
                for prev_books in combinations(range(k), i - k - 1):
                    if all(books[p][0] <= j - sum(books[q][0] for q in prev_books)) and max(dp[x][j - sum(books[y][0] for y in prev_books)] + books[prev_books[-1]][1] for x in range(k)):
                        dp[i][j] = min(dp[i][j], max(dp[k][j - books[k][0]] + books[k][1], dp[k][j]))
print(min(dp[-1]))
