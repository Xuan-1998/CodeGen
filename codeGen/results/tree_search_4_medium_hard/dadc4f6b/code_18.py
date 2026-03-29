import math

n, q, c = map(int, input().split())
stars = []
for _ in range(n):
    x, y, s_i = map(int, input().split())
    stars.append((x, y, s_i))

dp = [[[0] * (q+1) for _ in range(c+1)] for _ in range(n)]

for i in range(n):
    x, y, s_i = stars[i]
    t_0 = 10**9
    for k in range(q+1):
        if k == 0:
            dp[i][c][k] = min(c, s_i)
        else:
            dp[i][min(c, int(s_i * math.exp(-k / t_0)))[k-1] = dp[i][min(c, int(s_i * math.exp(-k / t_0)))[k]

for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    total_brightness = 0
    for i in range(n):
        if x1 <= stars[i][0] <= x2 and y1 <= stars[i][1] <= y2:
            total_brightness += dp[i][min(c, int(stars[i][2] * math.exp(-_ / t_0)))[k]
    print(total_brightness)
