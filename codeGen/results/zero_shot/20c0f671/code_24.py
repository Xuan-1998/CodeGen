# Iterate through the sorted books
while books:
    # Pop the tallest book from the heap
    height, thickness = heappop(books)

    # Find the shelf with the most available space
    target_shelf_height = float('inf')
    for i, shelf in enumerate(shelves):
        if shelf[1] >= height:
            target_shelf_height = min(target_shelf_height, shelf[0])
            break

    # Add the book to the target shelf
    if not shelves or target_shelf_height > shelves[-1][0]:
        shelves.append([height, 0])  # Create a new shelf with the book's height
    else:
        for i, shelf in enumerate(shelves):
            if shelf[0] == target_shelf_height:
                shelf[1] += thickness  # Add the book to the existing shelf
                break

# Calculate the minimum possible height of the bookcase
min_height = sum([shelf[0] for shelf in shelves])

print(min_height)  # Print the answer to stdout
