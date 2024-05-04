import sys

# Read input
books = []
shelf_width = 0
for _ in range(int(input())):
    thickness, height = map(int, input().split())
    books.append((thickness, height))
    shelf_width = max(shelf_width, thickness)

# Sort books by their heights in descending order
books.sort(key=lambda x: x[1], reverse=True)

# Initialize shelves
shelves = [(0, 0)]

# Place books on shelves
for book in books:
    for i, (shelf_height, shelf_capacity) in enumerate(shelves):
        if book[0] <= shelf_capacity:
            shelves[i] = (shelf_height + book[1], shelf_capacity)
            break
    else:
        shelves.append((book[1], book[0]))

# Calculate the minimum possible height
min_height = max(shelf[0] for shelf in shelves)

print(min_height)
