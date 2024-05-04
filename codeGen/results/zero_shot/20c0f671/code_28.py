import sys

books = []
shelf_width = 0

for _ in range(int(sys.stdin.readline().strip())):
    thickness, height = map(int, sys.stdin.readline().split())
    books.append((thickness, height))

shelf_width = int(sys.stdin.readline().strip())

books.sort(key=lambda x: x[1], reverse=True)

bookcase = []
current_shelf_width = 0
current_shelf_height = 0

for book in books:
    while current_shelf_width + book[0] > shelf_width:
        # Start a new shelf
        bookcase.append((current_shelf_height, 0))
        current_shelf_width = book[0]
        current_shelf_height = book[1]

    if current_shelf_height < book[1]:
        # Update the current shelf's height
        current_shelf_height = book[1]

min_height = max(shelf[0] for shelf in bookcase)
print(min_height)
