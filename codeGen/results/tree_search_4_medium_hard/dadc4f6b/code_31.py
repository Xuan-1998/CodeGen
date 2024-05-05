def solve():
    n, q, c = map(int, input().split())
    stars = [list(map(int, input().split())) for _ in range(n)]
    views = [list(map(int, input().split())) for _ in range(q)]

    dp = [[[0] * 101 for _ in range(101)] for _ in range(max(t) + 1)]

    for i, (x, y, s) in enumerate(stars):
        tmax = min(c - s, max(x, y))
        for t in range(tmax + 1):
            dp[t][x][y] += s

    ans = []
    for x1, y1, x2, y2 in views:
        ans.append(max(dp[time][min(x1, x2)][min(y1, y2)] for time in range(c)))

    print(*ans, sep='\n')

if __name__ == "__main__":
    solve()
