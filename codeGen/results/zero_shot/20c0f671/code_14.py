import sys

books = []
for _ in range(int(input())):
    thickness, height = map(int, input().split())
    books.append((thickness, height))

books.sort(key=lambda x: x[1], reverse=True)

shelf_width = int(input())

shelves = []
total_height = 0

for book in books:
    if not shelves or sum(shelf[1] for shelf in shelves) + book[0] <= shelf_width:
        # Add book to current shelf
        if not shelves:
            shelves.append([book])
        else:
            last_shelf = shelves[-1]
            if sum(last_shelf) + book[0] <= shelf_width:
                last_shelf.append(book)
            else:
                # Create a new shelf with the current book
                shelves.append([book])
    else:
        # Start a new shelf with the current book
        shelves.append([book])

total_height = sum(max(shelf[1] for shelf in shelves))
print(total_height)
