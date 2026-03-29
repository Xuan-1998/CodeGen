# Read input
books = []
shelf_width = 0
for _ in range(int(input())):
    thickness, height = map(int, input().split())
    books.append((thickness, height))
shelf_width = int(input())

# Sort books by thickness
books.sort(key=lambda x: x[0])

# Initialize result and current shelf height
result = 0
current_shelf_height = 0

# Iterate over the books
for thickness, height in books:
    # If the book can fit on the current shelf
    if thickness + current_shelf_height <= shelf_width:
        # Update the current shelf height
        current_shelf_height += height
    else:
        # Add the current shelf height to the result and reset the current shelf height
        result += current_shelf_height
        current_shelf_height = height
    
# Add the last shelf height to the result
result += current_shelf_height

print(result)
