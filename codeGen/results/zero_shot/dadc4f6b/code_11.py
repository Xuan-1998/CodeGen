code
total_brightness = 0
for view in views:
    t, x1, y1, x2, y2 = view[0]
    for star in stars:
        sx, sy, si = star
        if (x1 <= sx <= x2) and (y1 <= sy <= y2):
            total_brightness += si
    print(total_brightness)
