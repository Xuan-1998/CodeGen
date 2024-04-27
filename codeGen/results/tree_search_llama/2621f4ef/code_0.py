import sys

# Read the number of mines (n)
n = int(input())

# Initialize variables to store the minimum and maximum x and y coordinates
min_x, min_y, max_x, max_y = sys.maxsize, sys.maxsize, -sys.maxsize, -sys.maxsize

# Iterate through each mine's coordinates
for _ in range(n):
    x, y = map(int, input().split())
    
    # Update the minimum and maximum x and y coordinates
    min_x, min_y = min(min_x, x), min(min_y, y)
    max_x, max_y = max(max_x, x), max(max_y, y)

# Calculate the area of the smallest enclosing rectangle (city)
area = abs(max_x - min_x) * abs(max_y - min_y)

print(area)
