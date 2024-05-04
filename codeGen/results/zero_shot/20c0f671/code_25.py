import sys

books = []
for _ in range(1000):  # assuming at most 1,000 books
    thickness, height = map(int, sys.stdin.readline().split())
    books.append((thickness, height))

books.sort(key=lambda x: x[1], reverse=True)

shelves = []
current_shelf = []

for book in books:
    if sum(thickness for thickness, _ in current_shelf) + book[0] > shelf_width:
        shelves.append(current_shelf)
        current_shelf = [book]
    else:
        current_shelf.append(book)

shelves.append(current_shelf)

total_height = sum(max(height for _, height in shelf) for shelf in shelves)

print(total_height)
