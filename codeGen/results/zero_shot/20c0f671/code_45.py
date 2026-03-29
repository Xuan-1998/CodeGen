shelves = []
for book in books:
    thickness, height = book
    # Find a shelf with enough width for the book
    for i, shelf in enumerate(shelves):
        if shelf[0] + thickness <= 1000:  # Shelf width constraint
            shelves[i].append(height)  # Add book to existing shelf
            break
    else:
        # No shelf found, create a new one
        shelves.append([height])

# Calculate the total height of the bookcase
total_height = sum(max(shelf) for shelf in shelves)

print(total_height)
