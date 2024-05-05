import sys

n = int(sys.stdin.readline())
q = int(sys.stdin.readline())
c = int(sys.stdin.readline())

stars = []
for i in range(n):
    x, y, si = map(int, sys.stdin.readline().split())
    stars.append((x, y, si))

views = []
for i in range(q):
    t, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    views.append((t, (x1, y1), (x2, y2)))

def calculate_brightness(star_coords, view_coords, t):
    distances = []
    for x, y in star_coords:
        dx = max(0, view_coords[1][0] - x)
        dy = max(0, view_coords[1][1] - y)
        distances.append((dx**2 + dy**2)**0.5)

    filtered_stars = [(x, y, si) for (x, y), si in zip(star_coords, [s for _, _, s in star_coords]) if dx <= x2 - x1 and dy <= y2 - y1]

    brightnesses = []
    for x, y, si in filtered_stars:
        dt = (t - views[i][0])**2 / 10**9
        if dt < 1:
            brightnesses.append(si * (1 - dt))
        else:
            brightnesses.append(0)

    return sum(brightnesses)

brightnesses = []
for i, (t, _, ((x1, y1), (x2, y2))) in enumerate(views):
    total_brightness = 0
    for star_coords, si in zip(stars, [s for _, _, s in stars]):
        total_brightness += calculate_brightness([star_coords], [(x1, y1), (x2, y2)], t)
    brightnesses.append(total_brightness)

for brightness in brightnesses:
    print(brightness)
