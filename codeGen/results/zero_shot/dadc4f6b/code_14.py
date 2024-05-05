import sys

def solve_problem():
    # Read input
    n, q, c = map(int, sys.stdin.readline().split())
    stars = []
    for _ in range(n):
        x, y, s_i = map(int, sys.stdin.readline().split())
        stars.append((x, y, s_i))

    views = []
    for _ in range(q):
        t, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        views.append((t, (x1, y1), (x2, y2)))

    # Calculate total brightness of stars in each view
    result = []
    for view in views:
        t, (x1, y1), (x2, y2) = view
        total_brightness = 0
        for star in stars:
            x, y, s_i = star
            if x1 <= x <= x2 and y1 <= y <= y2:
                brightness = min(c, s_i + t)
                total_brightness += brightness
        result.append(total_brightness)

    # Print output
    for i, r in enumerate(result):
        print(r)
