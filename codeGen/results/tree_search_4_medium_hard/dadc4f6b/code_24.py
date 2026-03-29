import sys

def solve():
    n, q, c = map(int, input().split())
    stars = []
    for _ in range(n):
        x, y, s = map(int, input().split())
        stars.append((x, y, s))

    dp = [[0] * (c + 1) for _ in range(q + 1)]

    for i, ((x1, y1), (x2, y2)) in enumerate(map(lambda: map(int, input().split()), range(q))):
        for j in range(x1, x2 + 1):
            for k in range(y1, y2 + 1):
                if stars[j-1][2] <= c:
                    dp[i][j][k] = max(dp[i][j-1][k-1], stars[j-1][2] + dp[i-1][j-1][k-1])
                else:
                    dp[i][j][k] = dp[i-1][j][k]

    for _ in range(q):
        t, x1, y1, x2, y2 = map(int, input().split())
        total_brightness = 0
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if stars[i-1][2] <= c:
                    total_brightness += dp[_, i][j]
        print(total_brightness)

if __name__ == "__main__":
    solve()
