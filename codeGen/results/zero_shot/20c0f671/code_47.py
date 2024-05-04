import heapq

books = [list(map(int, input().split())) for _ in range(int(input()))]
shelf_width = int(input())

# Sort books by height
books.sort(key=lambda x: x[1], reverse=True)

shelves = []

for book in books:
    if not shelves or shelves[-1][0] >= book[0]:
        if len(shelves) > 0 and book[1] <= shelves[-1][1]:
            heapq.heappop(shelves)
        heapq.heappush(shelves, (book[0], book[1]))
    else:
        heapq.heappush(shelves, (book[0], book[1]))

print(max(shelf[1] for shelf in shelves))
