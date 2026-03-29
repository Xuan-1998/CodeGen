import sys

def solve():
    n, q, c = map(int, input().split())
    stars = []
    for _ in range(n):
        x, y, s = map(int, input().split())
        stars.append((x, y, s))

    views = []
    for _ in range(q):
        t, x1, y1, x2, y2 = map(int, input().split())
        views.append((t, (x1, y1), (x2, y2)))

    dp = {0: 0}
    for view in views:
        t, ((x1, y1), (x2, y2)) = view
        total_brightness = 0
        for star in stars:
            x, y, s = star
            if min(x1, y1) <= x < max(x2, y2) and min(y1, x1) <= y < max(y2, x2):
                brightness = abs(t - s / c) % c
                total_brightness += brightness
        dp[t] = dp.get(t-1, 0) + total_brightness

    for t in sorted(dp.keys()):
        print(dp[t])

if __name__ == "__main__":
    solve()
