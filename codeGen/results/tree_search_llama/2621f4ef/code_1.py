import sys

def find_min_area():
    n = int(sys.stdin.readline())
    
    # Initialize variables for minimum area calculation
    min_length, min_width = float('inf'), float('inf')
    
    # Read coordinates of all mines
    mine_coords = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        mine_coords.append((x, y))
    
    # Iterate through each possible city size (length and width)
    for length in range(1, max(max(x, y) - min(min(x, y)) + 1 for x, y in mine_coords) + 1):
        for width in range(1, max(max(y2-y1 for x1, y1 in mine_coords) + 1 for x2, y2 in mine_coords) + 1):
            # Check if all mines are within the current city size
            if all(min_x <= x <= max_x and min_y <= y <= max_y for (x, y), (min_x, min_y), (max_x, max_y) in zip(mine_coords, [(0, 0), (length-1, 0), (0, width-1), (length-1, width-1)])):
                # Update minimum area if the current city size is smaller
                if length * width < min_length * min_width:
                    min_length, min_width = length, width
    
    # Print the minimum possible area of the city
    print(min_length * min_width)

find_min_area()
