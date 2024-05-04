import sys
from collections import namedtuple

Book = namedtuple('Book', 'thickness height')
ShelfWidth = int(input())

books = []
for _ in range(int(input())):
    thickness, height = map(int, input().split())
    books.append(Book(thickness, height))

dp = [[float('inf')] * (ShelfWidth + 1) for _ in range(len(books) + 1)]

dp[0][0] = 0

for i in range(1, len(books) + 1):
    for w in range(1, ShelfWidth + 1):
        if books[i - 1].thickness <= w:
            dp[i][w] = min(dp[i - 1][w], dp[i - 1][max(0, w - books[i - 1].thickness)] + books[i - 1].height)
        else:
            dp[i][w] = dp[i - 1][w]

print(min(dp[-1]))
