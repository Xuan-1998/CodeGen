import sys

books = []
for _ in range(int(sys.stdin.readline())):
    thickness, height = map(int, sys.stdin.readline().split())
    books.append((thickness, height))
shelf_width = int(sys.stdin.readline())

books.sort(key=lambda x: x[0])

shelves = []
shelf_heights = [0]

for book in books:
    for i, shelf in enumerate(shelf_heights):
        if sum(b[0] for b in shelves[i]) + book[0] <= shelf_width:
            shelves.append(book)
            shelf_heights[i] = max(shelf_heights[i], book[1])
            break
    else:
        shelves.append([book])
        shelf_heights.append(book[1])

min_height = max(shelf_heights)
print(min_height)
