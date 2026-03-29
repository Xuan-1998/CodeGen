import sys

# Read input from stdin
books = []
shelf_width = None
for line in sys.stdin:
    if not line.strip():
        break
    thickness, height = map(int, line.split())
    books.append((thickness, height))

shelf_width = int(sys.stdin.readline())

# Sort books by thickness
books.sort(key=lambda x: x[0], reverse=True)

# Initialize variables
shelves = []
total_height = 0

for book in books:
    thickness, height = book
    # Find a shelf to place the book on
    for i, shelf in enumerate(shelves):
        if sum(x[0] for x in shelf) + thickness <= shelf_width:
            # Add the book to the shelf and update total_height
            shelf.append(book)
            total_height += height
            break
    else:
        # Create a new shelf
        shelves.append([book])
        total_height += height

print(total_height)
