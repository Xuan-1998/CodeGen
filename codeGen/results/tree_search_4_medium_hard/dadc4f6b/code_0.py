code
from collections import defaultdict

def solve():
    n, q, c = map(int, input().split())
    stars = []
    for _ in range(n):
        x, y, s = map(int, input().split())
        stars.append((x, y, s))

    dp = defaultdict(list)
    dp[0].append(0)

    for i in range(q):
        t, x1, y1, x2, y2 = map(int, input().split())
        visible_stars = []
        for star in stars:
            if min(x1, star[0]) <= star[0] <= max(x2, star[0]) and \
               min(y1, star[1]) <= star[1] <= max(y2, star[1]):
                visible_stars.append(star)

        total_brightness = sum(s for _, _, s in visible_stars)
        dp[t].append(total_brightness)

    return '\n'.join(map(str, dp[-1]))

print(solve())
code
