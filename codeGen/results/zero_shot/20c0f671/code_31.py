import sys

books = []
for _ in range(int(input())):
    thickness, height = map(int, input().split())
    books.append((height, thickness))

books.sort()

shelf_width = int(input())
current_shelf_width = 0
current_shelf_height = 0
total_height = 0

for height, thickness in books:
    if current_shelf_width + thickness > shelf_width:
        total_height += max(current_shelf_height, height)
        current_shelf_width = 0
        current_shelf_height = 0
    else:
        current_shelf_width += thickness
        current_shelf_height = max(current_shelf_height, height)

total_height += max(current_shelf_height, height)

print(total_height)
