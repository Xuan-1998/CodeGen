import sys
from collections import defaultdict

def solve():
    n, q = map(int, input().split())
    stars = []
    for _ in range(n):
        x, y, s = map(int, input().split())
        stars.append((x, y, s))

    views = []
    for _ in range(q):
        t, x1, y1, x2, y2 = map(int, input().split())
        views.append(((t, (x1, y1), (x2, y2)), 0))

    dp_states = defaultdict(lambda: defaultdict(int))
    for i, ((t, r), total_brightness) in enumerate(sorted(views)):
        t, ((x1, y1), (x2, y2)) = r
        if i == 0:
            continue

        prev_t, _ = views[i-1][0]
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if (prev_x <= x < x2 or x1 <= x and x < prev_x) and (prev_y <= y < y2 or y1 <= y and y < prev_y):
                    total_brightness += dp_states[(t-1, r)][(x1, y1), (x2, y2)]
                else:
                    for star in stars:
                        if star[0] == x and star[1] == y:
                            total_brightness += star[2]
        views[i][1] = total_brightness

    return '\n'.join(map(str, [view[1] for view in views]))

print(solve())
