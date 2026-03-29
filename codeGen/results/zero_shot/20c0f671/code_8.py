# Input books and shelf width
books = []
shelf_width = 0
with open('input.txt', 'r') as f:
    for line in f:
        thickness, height = map(int, line.split())
        books.append((thickness, height))
        if not shelf_width:
            shelf_width = thickness

# Sort books by height in descending order
books.sort(key=lambda x: x[1], reverse=True)

# Initialize the minimum possible bookcase height and the current shelf height
min_bookcase_height = 0
current_shelf_height = 0

# Iterate over the sorted books
for book in books:
    if book[0] <= shelf_width:
        # If the book can fit on the current shelf, add it to the shelf
        current_shelf_height += book[1]
    else:
        # If the book cannot fit on the current shelf, start a new shelf and add the book to it
        min_bookcase_height = max(min_bookcase_height, current_shelf_height)
        current_shelf_height = book[1]

# Add the height of the last shelf to the minimum possible bookcase height
min_bookcase_height = max(min_bookcase_height, current_shelf_height)

print(min_bookcase_height)
