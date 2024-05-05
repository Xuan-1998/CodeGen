n, q, c = map(int, input().split())
stars = []
for _ in range(n):
    x, y, s = map(int, input().split())
    stars.append((x, y, s))

views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    views.append((t, (x1, y1), (x2, y2)))

total_brightnesses = []
for view in views:
    t, ((x1, y1), (x2, y2)) = view
    total_brightness = 0
    for star in stars:
        sx, sy, ss = star
        if x1 <= sx <= x2 and y1 <= sy <= y2:
            total_brightness += ss
    print(total_brightness)
