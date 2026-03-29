import sys

def solve():
    n, q, c = map(int, input().split())
    stars = [list(map(int, input().split())) for _ in range(n)]
    views = []
    for _ in range(q):
        t, x1, y1, x2, y2 = map(int, input().split())
        views.append((t, (x1, y1), (x2, y2)))

    dp = [[0] * 101 for _ in range(101)]
    for star in stars:
        s, x1, y1 = star
        if s <= c:
            for view in views:
                t, (x3, y3), (x4, y4) = view
                if x1 <= x3 and x2 >= x4 and y1 <= y3 and y2 >= y4:
                    dp[min(x2, x4)][min(y2, y4)] += s

    for i in range(100, -1, -1):
        for j in range(100, -1, -1):
            if i > 0: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if j > 0 and i > 0:
                dp[i][j] += min(dp[i-1][j-1], c)
    res = []
    for view in views:
        t, (x1, y1), (x2, y2) = view
        res.append(str(min(x2, 100) * min(y2, 100) - dp[min(x2, 100)][min(y2, 100)] + dp[0][0]))
    print('\n'.join(res))

if __name__ == "__main__":
    solve()
