# Step 2: Calculate Total Brightness
for view in views:
    t, (x1, y1), (x2, y2) = view
    total_brightness = 0
    for star in stars:
        x, y, s = star
        if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
            total_brightness += s
    print(total_brightness)
