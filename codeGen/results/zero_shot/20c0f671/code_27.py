import sys

books = []
shelf_width = 0

for _ in range(int(input())):
    thickness, height = map(int, input().split())
    books.append((thickness, height))

shelf_width = int(input())

books.sort(key=lambda x: x[1], reverse=True)

shelves = []
current_shelf = []

for book in books:
    if sum(book[0] for book in current_shelf) + book[0] <= shelf_width:
        current_shelf.append(book)
    else:
        shelves.append(current_shelf)
        current_shelf = [book]

total_height = sum(max(book[1] for book in shelf) for shelf in shelves)

print(total_height)
