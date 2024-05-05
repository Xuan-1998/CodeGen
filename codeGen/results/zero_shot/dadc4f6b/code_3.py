n, q, c = map(int, input().split())
stars = []
for _ in range(n):
    x, y, s = map(int, input().split())
    stars.append((x, y, s))
views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    views.append((t, (x1, y1), (x2, y2)))

star_dict = {}
for star in stars:
    x, y, s = star
    if (x, y) not in star_dict:
        star_dict[(x, y)] = [s]
    else:
        star_dict[(x, y)].append(s)

for view in views:
    t, (x1, y1), (x2, y2) = view
    total_brightness = 0
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if (x, y) in star_dict:
                brightnesses = star_dict[(x, y)]
                total_brightness += min(brightnesses)
print(total_brightness)
