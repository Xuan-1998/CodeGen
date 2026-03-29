dp = [[[0] * 101 for _ in range(101)] for _ in range(q + 1)]

stars = []
for _ in range(n):
    x, y, s = map(int, input().split())
    stars.append((x, y, s))

for i in range(q):
    t, x1, x2, y1, y2 = map(int, input().split())
    for j in range(y1 - 1, y2):
        dp[i][min(x1, stars[j][0])][y1] += min(c, stars[j][2])
        if max(x2, stars[j][0]) <= 100:
            dp[i][max(x2, stars[j][0]), y1] += min(c, stars[j][2])

for i in range(q):
    print(sum(dp[i][x1][y1] for x1 in range(1, 101) for y1 in range(1, 101)))
