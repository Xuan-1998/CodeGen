n = int(input())  # number of stars
q = int(input())  # number of views

stars = []  # list of star coordinates and initial brightness
for _ in range(n):
    x, y, s = map(int, input().split())
    stars.append((x, y, s))

views = []  # list of view times and coordinates
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    views.append((t, (x1, y1), (x2, y2)))

for view in views:
    t, (x1, y1), (x2, y2) = view
    brightness = 0
    for star in stars:
        x, y, s = star
        if x1 <= x <= x2 and y1 <= y <= y2:  # check if the star is within the view
            brightness += min(s, c)
    print(brightness)
