import sys

def total_brightness(n, q, stars, views):
    # Initialize the total brightness for each view to 0
    total_brightnesses = [0] * q
    
    # Iterate over each view
    for i in range(q):
        # Extract the coordinates of the lower left and upper right corners of the rectangle
        x1, y1, x2, y2 = views[i]
        
        # Initialize the brightness for this view to 0
        brightness = 0
        
        # Iterate over each star
        for j in range(n):
            # Check if the star is within the current view
            if (x1 <= stars[j][0] <= x2) and (y1 <= stars[j][1] <= y2):
                # Add the brightness of this star to the total brightness for this view
                brightness += stars[j][2]
        
        # Update the total brightness for this view
        total_brightnesses[i] = brightness
    
    return total_brightnesses

# Read the input from stdin
n, q, c = map(int, sys.stdin.readline().split())
stars = []
for _ in range(n):
    x, y, s = map(int, sys.stdin.readline().split())
    stars.append((x, y, s))
views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    views.append((x1, y1, x2, y2))

# Calculate the total brightness for each view
total_brightnesses = total_brightness(n, q, stars, views)

# Print the output to stdout
for brightness in total_brightnesses:
    print(brightness)
