# Step 1: Define variables
max_shelf_width = int(input())  # Get the maximum shelf width from input
books = []  # Initialize an empty list of books
heights = []  # Initialize an empty list to store book heights

# Step 2: Read and process each book
for _ in range(int(input())):  # Number of books
    thickness, height = map(int, input().split())  # Get the book's thickness and height
    books.append((thickness, height))  # Add book details to the list
    heights.append(height)  # Store the book height for later use

# Step 3: Sort books by their height in descending order
books.sort(key=lambda x: x[1], reverse=True)

# Step 4: Initialize variables for dynamic programming
dp = [float('inf')] * (max_shelf_width + 1)  # Initialize a table for minimum heights
dp[0] = 0  # The height of the bookcase with no books is 0

# Step 5: Fill the dynamic programming table
for i, (thickness, _) in enumerate(books):
    for j in range(max_shelf_width, thickness - 1, -1):  # Iterate from max width to book thickness
        dp[j] = min(dp[j], dp[j - thickness] + height)  # Update the minimum height

# Step 6: Find and output the minimum possible height of the bookcase
min_height = float('inf')
for i in range(max_shelf_width + 1):
    if dp[i] < height:
        min_height = dp[i]
        break

print(min_height)
