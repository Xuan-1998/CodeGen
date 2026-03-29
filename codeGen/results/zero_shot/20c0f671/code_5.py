import sys

# Read input
n = int(sys.stdin.readline())  # number of books
books = []
for _ in range(n):
    thickness, height = map(int, sys.stdin.readline().split())
    books.append((thickness, height))
shelf_width = int(sys.stdin.readline())

# Sort books by thickness
books.sort(key=lambda x: x[0])

shelves = []
shelf_heights = [0]

for thickness, height in books:
    # Find the first shelf that can hold this book
    for i, shelf_height in enumerate(shelf_heights):
        if thickness + shelf_height <= shelf_width:
            shelves.append(height)
            break
    else:  # no such shelf exists, create a new one
        shelves.append(height)

# Calculate the minimum total height
total_height = sum(shelves)
print(total_height)
