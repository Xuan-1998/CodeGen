# Sort stars by their initial brightness
stars.sort(key=lambda x: x[2], reverse=True)

total_brightness = 0
for t, (x1, y1), (x2, y2) in views:
    current_brightness = 0
    for star in stars:
        if x1 <= star[0] <= x2 and y1 <= star[1] <= y2:
            current_brightness += star[2]
    total_brightness += current_brightness

# Print the results
for brightness in [current_brightness]:
    print(brightness)
