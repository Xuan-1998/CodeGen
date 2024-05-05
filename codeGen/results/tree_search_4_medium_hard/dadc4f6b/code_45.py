import sys

n, q, c = map(int, input().split())
stars = []
for _ in range(n):
    x, y, s = map(int, input().split())
    stars.append((x, y, s))

views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    views.append((t, x1, y1, x2, y2))

dp = [[0] * (n+1) for _ in range(q)]

# Initialize dp[0][j] to s_j * c
for j in range(n):
    dp[0][j] = stars[j][2] * c

for t in range(1, q):
    for j in range(n):
        total_brightness = 0
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if (x, y) in [(star[0], star[1]) for star in stars]:
                    total_brightness += star[2] * c
        dp[t][j] = max(dp[t-1][j], total_brightness)

print(max(dp[-1]))
