import sys

# Read input from stdin
n = int(sys.stdin.readline())
mines = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    mines.append((x, y))

# Find the minimum and maximum coordinates for each axis
min_x, max_x = float('inf'), float('-inf')
min_y, max_y = float('inf'), float('-inf')

for x, y in mines:
    min_x, max_x = min(min_x, x), max(max_x, x)
    min_y, max_y = min(min_y, y), max(max_y, y)

# Calculate the city's area
city_area = (max_x - min_x) * (max_y - min_y)

# Print the answer to stdout
print(city_area)
