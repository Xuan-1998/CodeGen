import sys

books = []
for book in range(int(sys.stdin.readline())):
    thickness, height = map(int, sys.stdin.readline().split())
    books.append((height, thickness))
books.sort(reverse=True)

shelf_width = int(sys.stdin.readline())

shelves = [[], [], []]  # Initialize shelves with empty lists
current_shelf = 0

for book in books:
    height, thickness = book
    if thickness > shelf_width:
        continue  # Book too thick for current shelf
    while thickness > len(shelves[current_shelf]):
        if current_shelf == len(shelves) - 1:
            break  # No more shelves, cannot place book
        current_shelf += 1
    shelves[current_shelf].append((height, thickness))

total_height = 0
for shelf in shelves:
    total_height += max(book[0] for book in shelf)
print(total_height)
