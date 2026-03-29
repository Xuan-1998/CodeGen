import sys

n, q, c = map(int, sys.stdin.readline().split())
stars = []
for _ in range(n):
    x, y, si = map(int, sys.stdin.readline().split())
    stars.append((x, y, si))

views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    views.append(((t, x1, y1, x2, y2), 0))  # Initialize brightness to 0 for each view

for star in stars:
    x, y, si = star
    for view in views:
        t, x1, y1, x2, y2 = view[0]
        if x1 <= x <= x2 and y1 <= y <= y2:  # Check if the star is within the view
            view[1] += min(c, si)  # Add the initial brightness of the star to the total brightness

for view in views:
    print(view[1])
