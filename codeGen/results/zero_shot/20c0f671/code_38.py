import sys

books = []
for line in sys.stdin:
    thickness, height = map(int, line.split())
    books.append((thickness, height))

books.sort(key=lambda x: x[1], reverse=True)

shelves = []
current_shelf_width = 0
total_height = 0

for thickness, height in books:
    if current_shelf_width + thickness <= shelf_width:
        total_height += height
        current_shelf_width += thickness
    else:
        shelves.append((total_height, current_shelf_width))
        total_height = height
        current_shelf_width = thickness

shelves.append((total_height, current_shelf_width))

minimum_height = sum(shelf[0] for shelf in shelves)
print(minimum_height)
