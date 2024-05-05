n, q, c = map(int, input().split())
stars = []
for _ in range(n):
    x, y, s = map(int, input().split())
    stars.append((x, y, s))
views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    views.append(((t, x1, y1), (x2, y2)))

star_brightness = []
for star in stars:
    x, y, s = star
    for view in views:
        t, (x1, y1), (x2, y2) = view
        if x1 <= x <= x2 and y1 <= y <= y2:  # Check if the star is within the view
            brightness = min(c, s + c * (t ** 0.5))  # Calculate the brightness of the star in this view
            star_brightness.append(brightness)

total_brightness = []
for i in range(len(views)):
    total = sum(star_brightness[i::len(views)])  # Calculate the total brightness of this view
    total_brightness.append(total)

for i, brightness in enumerate(total_brightness):
    print(brightness)
