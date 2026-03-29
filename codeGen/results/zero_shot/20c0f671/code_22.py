import heapq
n = int(input())
books = []
for _ in range(n):
    thickness, height = map(int, input().split())
    books.append((height, -thickness))  # Use negative thickness for sorting
max_width = int(input())

# Sort books by height and then by thickness (in descending order)
books.sort()

# Initialize the minimum height of the bookcase
min_height = 0

# Initialize the current shelf width and height
shelf_width = max_width
shelf_height = 0

# Iterate over the sorted books
for book_height, book_thickness in books:
    if book_thickness > shelf_width:  # If a book doesn't fit on the current shelf
        min_height += shelf_height  # Update the minimum height of the bookcase
        shelf_width = max_width  # Reset the shelf width and height
        shelf_height = 0

    if book_height + shelf_height > shelf_height:  # If this book would make the shelf too tall
        min_height += shelf_height  # Update the minimum height of the bookcase
        shelf_width = max_width  # Reset the shelf width and height
        shelf_height = 0

    else:
        shelf_height += book_height  # Add the book to the current shelf

# Add one more shelf for the last books that don't fit on any other shelf
min_height += shelf_height

print(min_height)
