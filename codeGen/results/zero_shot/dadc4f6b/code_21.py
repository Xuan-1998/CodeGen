n, q, c = map(int, input().split())
stars = []
for _ in range(n):
    x, y, si = map(int, input().split())
    stars.append((x, y, si))
views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    views.append((t, (x1, y1), (x2, y2)))

for view in views:
    t, (x1, y1), (x2, y2) = view
    total_brightness = 0
    for star in stars:
        x, y, si = star
        if x1 <= x <= x2 and y1 <= y <= y2:
            total_brightness += si
    print(total_brightness)
