from collections import defaultdict

c, n = map(int, input().split())
stars = []
for _ in range(n):
    x, y, s = map(int, input().split())
    stars.append((x, y, s))

views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    views.append((t, (x1, y1), (x2, y2)))

dp = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int))))

def calculate_brightness(t, (x1, y1), (x2, y2)):
    brightness = 0
    for star in stars:
        if x1 <= star[0] <= x2 and y1 <= star[1] <= y2:
            brightness += min(c, star[2])
    return brightness

for t, ((x1, y1), (x2, y2)) in enumerate(views):
    dp[t][x1][y1][x2][y2] = calculate_brightness(t, (x1, y1), (x2, y2))

for view in views:
    t, ((x1, y1), (x2, y2)) = view
    print(dp[t][x1][y1][x2][y2])
