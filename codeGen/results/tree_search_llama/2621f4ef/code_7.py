import sys

# Read input from stdin
n = int(sys.stdin.readline())
mines = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    mines.append((x, y))

# Sort the mines by their maximum coordinate value
mines.sort(key=lambda p: max(p[0], p[1]))

# Initialize minimum area and its corresponding city size
min_area = float('inf')
city_size = None

# Iterate over possible square sizes
for side in range(1, len(mines) + 1):
    # Check if the current square can cover all mines
    for i in range(len(mines)):
        x, y = mines[i]
        if (x >= side and y >= side) or (x <= -side and y <= -side):
            break
    else:
        continue
    # Update minimum area if necessary
    min_area = min(min_area, side ** 2)
    city_size = side

# Print the result
print(min_area)
