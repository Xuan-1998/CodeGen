import sys

books = []
while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    thickness, height = map(int, line.split())
    books.append((height, thickness))

books.sort(reverse=True)

shelves = []

for height, thickness in books:
    found_shelf = False
    for i, (shelf_height, shelf_books) in enumerate(shelves):
        if shelf_books + thickness <= 1000:  # assuming shelf_width is 1000
            shelves[i] = (max(shelf_height, height), shelf_books + thickness)
            found_shelf = True
            break
    if not found_shelf:
        shelves.append((height, thickness))

min_height = sum(shelf[0] for shelf in shelves)
print(min_height)
