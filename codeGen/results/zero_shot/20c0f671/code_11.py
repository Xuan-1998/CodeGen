import heapq
n, m = map(int, input().split())
books = []
for _ in range(n):
    t, h = map(int, input().split())
    books.append((t, h))
shelf_width = int(input())

# Sort the books by their height
books.sort(key=lambda x: x[1])

# Initialize the heap with the first book and its shelf
shelf_height = [0]
heap = [(h, i) for (i, (t, h)) in enumerate(books)]
while len(heap) > 1:
    # Get the tallest books from the top two shelves
    h1, i1 = heapq.heappop(heap)
    h2, i2 = heapq.heppop(heap)

    # If the combined thickness of the two books is less than or equal to the shelf width,
    # place them on the same shelf
    if t1 + t2 <= shelf_width:
        # Update the height of the current shelf
        shelf_height[-1] += h1 - h2
    else:
        # Place the taller book on a new shelf
        shelf_height.append(h1)
        heapq.heappush(heap, (h2, i2))

# The final height is the sum of the heights of all shelves
print(sum(shelf_height))
