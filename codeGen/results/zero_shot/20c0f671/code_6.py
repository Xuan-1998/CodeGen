# Read input
books = []
for _ in range(int(input())):
    thickness, height = map(int, input().split())
    books.append((thickness, height))

shelf_width = int(input())

# Sort books by height
books.sort(key=lambda x: x[1])

# Initialize shelves and current shelf height
shelves = [(0, 0)]  # (height, used width)
current_shelf_height = 0
current_shelf_used_width = 0

# Place books on shelves
for thickness, height in books:
    for i, (shelf_height, shelf_used_width) in enumerate(shelves):
        if shelf_used_width + thickness <= shelf_width:  # book can fit on this shelf
            if shelf_height < current_shelf_height or i == len(shelves) - 1:  # best to keep the book on this shelf
                current_shelf_height = shelf_height
                current_shelf_used_width = shelf_used_width + thickness
                break  # move on to next book
    else:  # no shelf has enough width, start a new one
        shelves.append((height, thickness))
        current_shelf_height = height
        current_shelf_used_width = thickness

# Print the minimum possible height of the bookcase
print(max(shelf[0] for shelf in shelves) + 1)
