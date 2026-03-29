import sys

def min_bookcase_height(books, shelf_width):
    # Sort books by height (descending)
    books.sort(key=lambda x: x[1], reverse=True)

    shelves = []
    shelf_height = 0
    shelf_books = []

    for book in books:
        if len(shelf_books) > 0 and sum(b[0] for b in shelf_books) + book[0] <= shelf_width:
            # Book can be placed on an existing shelf, update height and add to shelf
            shelf_height = max(shelf_height, book[1])
            shelf_books.append(book)
        else:
            # Create a new shelf with this book
            shelves.append((shelf_height, shelf_books))
            shelf_height = book[1]
            shelf_books = [book]

    # Calculate the total height of the bookcase
    return max(shelf_height for shelf_height, _ in shelves)

# Read input from stdin
books = []
for _ in range(int(sys.stdin.readline())):
    thickness, height = map(int, sys.stdin.readline().split())
    books.append((thickness, height))

shelf_width = int(sys.stdin.readline())

print(min_bookcase_height(books, shelf_width))
