import heapq

def min_bookcase_height(books, shelf_width):
    # Sort books by height in descending order
    books.sort(key=lambda x: x[1], reverse=True)

    # Initialize priority queue with an empty shelf
    shelves = [(0, 0)]  # (height, thickness)
    heapq.heapify(shelves)

    total_height = 0

    for book in books:
        while True:
            # Extract the top shelf from the priority queue
            height, thickness = heapq.heappop(shelves)

            # Check if we can add this book to the current shelf
            if thickness + book[0] <= shelf_width:
                break

            # If not, increment the total height and reset the shelf
            total_height += height
            height = 0
            thickness = 0

        # Add the new book to the current shelf
        height += book[1]
        thickness += book[0]

        # Push the updated shelf back into the priority queue
        heapq.heappush(shelves, (height, thickness))

    return total_height + height
