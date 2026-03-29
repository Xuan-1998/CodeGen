import sys
import heapq

books = []
for _ in range(int(sys.stdin.readline())):
    thickness, height = map(int, sys.stdin.readline().split())
    books.append((height, thickness))

books.sort()

shelf_queue = []
for _ in range(int(sys.stdin.readline())):
    max_width = int(sys.stdin.readline())
    heapq.heappush(shelf_queue, (0, max_width))

shelf_heights = []
while books:
    height, thickness = books.pop(0)
    while shelf_queue:
        max_height, max_width = heapq.heappop(shelf_queue)
        if thickness <= max_width:
            break
    else:
        # No shelves can accommodate this book, start a new one
        heapq.heappush(shelf_queue, (height, max_width))
    shelf_heights.append(height)

print(max(shelf_heights))
