import sys

n, q, c = map(int, sys.stdin.readline().split())
stars = []
for _ in range(n):
    x, y, s = map(int, sys.stdin.readline().split())
    stars.append((x, y, s))

views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    views.append(((x1, y1), (x2, y2), t))

total_brightness = 0
for view in views:
    lower_left, upper_right, _ = view
    for star in stars:
        if (star[0] >= lower_left[0] and star[0] <= upper_right[0] and
                star[1] >= lower_left[1] and star[1] <= upper_right[1]):
            total_brightness += star[2]
    print(total_brightness)
