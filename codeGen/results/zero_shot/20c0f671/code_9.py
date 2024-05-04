import sys

# Read input from stdin
num_books = int(sys.stdin.readline())
books = []
for _ in range(num_books):
    thickness, height = map(int, sys.stdin.readline().split())
    books.append((thickness, height))

# Sort the books by height
books.sort(key=lambda x: x[1])

shelves = []
current_shelf = []

for thickness, height in books:
    if sum(b[0] for b in current_shelf) + thickness <= shelf_width:
        current_shelf.append((thickness, height))
    else:
        shelves.append(current_shelf)
        current_shelf = [(thickness, height)]

total_height = sum(max(book[1] for book in shelf) for shelf in shelves)

print(total_height)
