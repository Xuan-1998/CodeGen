import sys

def min_bookcase_height(books, shelf_width):
    # Sort books by height in descending order
    books.sort(key=lambda x: x[1], reverse=True)

    bookcase_height = 0
    current_shelf_height = 0
    for book_thickness, book_height in books:
        if book_thickness + current_shelf_height <= shelf_width:
            # Book fits on current shelf, add its height to the shelf
            current_shelf_height += book_height
        else:
            # Book doesn't fit, start a new shelf
            bookcase_height += current_shelf_height
            current_shelf_height = book_height

    # Add the height of the last shelf
    bookcase_height += current_shelf_height

    return bookcase_height

# Read input from stdin
books = []
shelf_width = int(sys.stdin.readline())
for _ in range(int(sys.stdin.readline())):
    thickness, height = map(int, sys.stdin.readline().split())
    books.append((thickness, height))

# Calculate and print the result
bookcase_height = min_bookcase_height(books, shelf_width)
print(bookcase_height)
