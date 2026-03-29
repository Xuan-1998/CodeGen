for t, ((x1, y1), (x2, y2)) in views:
    total_brightness = 0
    for x, y, s_i in stars:
        if x1 <= x <= x2 and y1 <= y <= y2:
            total_brightness += min(s_i, c)
    print(total_brightness)
