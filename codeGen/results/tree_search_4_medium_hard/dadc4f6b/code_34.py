import sys
input = sys.stdin.readline

def solve():
    n, q, c = map(int, input().split())
    stars = []
    for _ in range(n):
        x, y, s = map(int, input().split())
        stars.append((x, y, s))

    dp = [[0] * 101 for _ in range(100001)]
    for t in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        for star in stars:
            if star[1] >= y1 and star[1] <= y2 and star[0] <= x2 and star[0] >= x1:
                dp[t][star[0]] += star[2]

    print(max(dp[-1]))

solve()
