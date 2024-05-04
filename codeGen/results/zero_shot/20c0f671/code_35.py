import sys

def calculate_height(books, shelf_width):
    # Sort the books by height in descending order
    books.sort(key=lambda x: x[1], reverse=True)

    # Initialize the total height and the current shelf width
    total_height = 0
    current_shelf_width = 0

    # Iterate over the sorted books
    for book in books:
        # If the book can fit on the current shelf, add its thickness to the shelf width
        if current_shelf_width + book[0] <= shelf_width:
            current_shelf_width += book[0]
        else:
            # Otherwise, start a new shelf and increment the total height
            total_height += book[1]
            current_shelf_width = book[0]

    # Add the height of the last shelf to the total height
    total_height += books[-1][1]

    return total_height

# Read input from stdin
n = int(sys.stdin.readline())
books = []
for _ in range(n):
    thickness, height = map(int, sys.stdin.readline().split())
    books.append((thickness, height))

shelf_width = int(sys.stdin.readline())

# Calculate and print the minimum possible height of the bookcase
min_height = calculate_height(books, shelf_width)
print(min_height)
