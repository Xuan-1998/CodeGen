# Step 1: Read the input
n, q, c = map(int, input().split())  # read n, q, and c
stars = []  # initialize a list to store stars
for i in range(n):
    x, y, s = map(int, input().split())
    stars.append((x, y, s))  # store the star's coordinates and initial brightness

views = []  # initialize a list to store views
for i in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())  # read view information
    views.append((t, (x1, y1), (x2, y2)))  # store the view's time and coordinates

# Step 2: Calculate the total brightness for each view
for view in views:
    t, ((lx, ly), (rx, ry)) = view
    total_brightness = sum(s if min(x, y) <= x1i <= max(x, y) and min(y1i, y2i) <= y1i <= max(y1i, y2i) else 0 for x1i, y1i in [(x, y) for (x, y), s in stars] for ((x, y), s) in stars)
    print(total_brightness)
