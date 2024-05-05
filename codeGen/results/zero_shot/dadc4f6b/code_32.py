import sys

# Step 1: Parse input data
n, q, c = map(int, sys.stdin.readline().split())
stars = []
for _ in range(n):
    x, y, s = map(int, sys.stdin.readline().split())
    stars.append((x, y, s))
views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    views.append((t, (x1, y1), (x2, y2)))

# Step 2: Initialize variables
total_brightnesses = {}

# Step 3: Calculate star brightness for each view
for t, ((x1, y1), (x2, y2)) in views:
    total_brightness = 0
    for x, y, s in stars:
        if x1 <= x <= x2 and y1 <= y <= y2:
            brightness = s - c * t
            total_brightness += brightness
    print(total_brightness)
