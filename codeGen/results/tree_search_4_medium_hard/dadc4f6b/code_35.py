c = int(input())
n = int(input())
stars = []
for _ in range(n):
    x, y, s = map(int, input().split())
    stars.append((x, y, s))

views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    views.append((t, x1, y1, x2, y2))

dp = [[[0] * (101)] * 101] * 101

def brightness(t, x, y):
    res = 0
    for star in stars:
        if star[0] <= x and star[1] <= y:
            res += min(c, star[2])
    return res

for t in range(q):
    t, x1, y1, x2, y2 = views[t]
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            dp[t][x][y] = brightness(t, x, y)

for t in range(q):
    print(dp[t][views[t][2]][views[t][4]])
