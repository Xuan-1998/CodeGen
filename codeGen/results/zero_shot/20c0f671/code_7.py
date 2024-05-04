import heapq

books = []
for _ in range(1000):
    thickness, height = map(int, input().split())
    books.append((height, thickness))

books.sort(reverse=True)

shelves = []
current_height = 0
current_shelf_width = int(input())  # maximum shelf width

for height, thickness in books:
    if thickness + sum(shelf) <= current_shelf_width:  # combined thickness is within shelf width
        shelves[-1].append(height)  # add to existing shelf
    else:
        shelves.append([height])  # create new shelf

    current_height = max(current_height, height)

total_height = sum(max(shelf) for shelf in shelves)

print(total_height)
