def total_brightness():
    n, q, c = map(int, input().split())
    stars = []
    for _ in range(n):
        x, y, s = map(int, input().split())
        stars.append((x, y, s))

    views = []
    for _ in range(q):
        t, x1, y1, x2, y2 = map(int, input().split())
        views.append((t, (x1, y1), (x2, y2)))

    for view in views:
        t, ((x1, y1), (x2, y2)) = view
        total_brightness_in_view = sum(s if x >= x1 and x <= x2 and y >= y1 and y <= y2 else 0 for x, y, s in stars)
        print(total_brightness_in_view)

total_brightness()
