import heapq
from collections import deque

# Read input
N = int(input())  # number of books
books = []
for _ in range(N):
    t, h = map(int, input().split())
    books.append((h, t))

shelf_width = int(input())

# Sort books
books.sort(reverse=True)

# Create a priority queue for shelves
shelves = []

# Process books
total_height = 0
for h, t in books:
    if not shelves or shelves[0][1] + t <= shelf_width:  # book can fit on an existing shelf
        heapq.heappush(shelves, (h, t))
    else:  # create a new shelf
        total_height += max([s[0] for s in shelves])  # add the height of the tallest previous shelf
        shelves = [(h, t)]

# Calculate total height
total_height += max([s[0] for s in shelves])

print(total_height)
