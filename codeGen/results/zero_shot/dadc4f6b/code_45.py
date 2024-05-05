# Step 1: Read input
n, q, c = map(int, input().split())
stars = []
for _ in range(n):
    x, y, s = map(int, input().split())
    stars.append((x, y, s))
views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    views.append((t, (x1, y1), (x2, y2)))

# Step 2: Sort stars by their coordinates
stars.sort(key=lambda star: (star[0], star[1]))

# Step 3: Process each view
for t, ((xl, yl), (xr, yr)) in views:
    # Initialize the total brightness for this view to 0
    total_brightness = 0
    
    # Iterate over all stars and check if they are within the current view
    for star in stars:
        x, y, s = star
        if xl <= x <= xr and yl <= y <= yr:
            # Calculate the brightness of this star at time t
            brightness = min(s + (c - 1), c)
            
            # Add the brightness to the total brightness for this view
            total_brightness += brightness
    
    # Print the total brightness for this view
    print(total_brightness)
