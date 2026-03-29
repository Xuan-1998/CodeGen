import heapq

def min_height_of_bookcase():
    # Read input from stdin
    N = int(input())
    books = []
    for _ in range(N):
        thickness, height = map(int, input().split())
        books.append((thickness, height))

    max_shelf_width = int(input())

    # Sort the books by their heights
    books.sort(key=lambda x: x[1])

    # Initialize a priority queue to store the shelves
    shelves = []
    heapq.heappush(shelves, 0)  # The height of an empty shelf is 0

    for book in books:
        while shelves and book[0] > max_shelf_width - shelves[0]:
            # If the current book cannot be placed on the top shelf
            # remove the top shelf and try to place the book again
            heapq.heappop(shelves)

        if shelves:
            # Update the height of the top shelf by adding the height of the book
            shelves[0] += book[1]
        else:
            # If there are no more shelves, create a new one with the height of the book
            heapq.heappush(shelves, book[1])

    return max(shelves)  # The minimum possible height of the bookcase is the maximum shelf height

print(min_height_of_bookcase())
