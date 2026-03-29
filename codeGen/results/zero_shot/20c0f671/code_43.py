import sys

# Read input from stdin
books = []
shelf_width = 0
for line in sys.stdin:
    line = line.strip().split()
    books.append((int(line[0]), int(line[1])))
    shelf_width = max(shelf_width, int(line[0]))

# Sort books by height in descending order
books.sort(key=lambda x: x[1], reverse=True)

# Initialize the shelf stack
shelves = []

# Your turn! What's the next step?
