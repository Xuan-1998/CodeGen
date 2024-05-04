# Initialize an empty list to represent the shelves
shelves = []

for book in books:
    # Try to find a shelf with enough space
    for i, shelf in enumerate(shelves):
        if sum(book[0] for book in shelf) + book[0] <= shelf_width:
            # Add the book to the existing shelf
            shelves[i].append(book)
            break
    else:
        # Create a new shelf for this book
        shelves.append([book])

# Calculate the total height of the bookcase
total_height = 0
for shelf in shelves:
    total_height += max(book[1] for book in shelf)

print(total_height)
