n, q = map(int, input().split())
stars = []
for _ in range(n):
    x, y, s = map(int, input().split())
    stars.append((x, y, s))

views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    views.append(((x1, y1), (x2, y2)))

for (x1, y1), (x2, y2) in views:
    total_brightness = 0
    for star in stars:
        if x1 <= star[0] <= x2 and y1 <= star[1] <= y2:  # check if the star is within the view
            total_brightness += star[2]
    print(total_brightness)
