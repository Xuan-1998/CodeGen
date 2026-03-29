import sys

books = []
for _ in range(int(input())):
    thickness, height = map(int, input().split())
    books.append((thickness, height))

books.sort(key=lambda x: x[1], reverse=True)

shelves = []
current_shelf = []
total_thickness = 0

for book in books:
    if total_thickness + book[0] <= max_shelf_width:
        current_shelf.append(book)
        total_thickness += book[0]
    else:
        shelves.append(current_shelf)
        current_shelf = [book]
        total_thickness = book[0]

if current_shelf:
    shelves.append(current_shelf)

max_shelf_height = 0

for shelf in shelves:
    max_shelf_height = max(max_shelf_height, max(book[1] for book in shelf))

print(max_shelf_height)
