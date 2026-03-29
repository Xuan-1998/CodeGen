import sys

books = []
for _ in range(int(input())):
    books.append(list(map(int, input().split())))

shelfWidth = int(input())

print(minHeightShelves(books, shelfWidth))
