import sys

n = int(sys.stdin.readline())
q = int(sys.stdin.readline())
c = int(sys.stdin.readline())

stars = []
for _ in range(n):
    x, y, s = map(int, sys.stdin.readline().split())
    stars.append((x, y, s))

views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    views.append((t, (x1, y1), (x2, y2)))

def calculate_brightness(stars, view):
    t, (x1, y1), (x2, y2) = view
    brightness = 0
    for star in stars:
        x, y, s = star
        if x1 <= x <= x2 and y1 <= y <= y2:  # check if the star is within the view's rectangle
            brightness += s
    return brightness

for view in views:
    t, (x1, y1), (x2, y2) = view
    brightness = calculate_brightness(stars, view)
    print(brightness)
