def solve(input):
    n, q, c = map(int, input().split())
    stars = []
    for _ in range(n):
        x, y, s = map(int, input().split())
        stars.append((x, y, s))

    dp = [[[0] * (101) for _ in range(101)] for _ in range(q+1)]

    for t in range(q+1):
        for i in range(len(stars)):
            x1, y1, s = stars[i]
            x2, y2 = min(x1 + 100, 100), min(y1 + 100, 100)
            if t == 0:
                dp[t][x1][y1] += s
            else:
                for x in range(max(1, x1-100), min(x2+1, 101)):
                    for y in range(max(1, y1-100), min(y2+1, 101)):
                        dp[t][x][y] = max(dp[t][x][y], dp[t-1][max(0, x-x1)][max(0, y-y1)] + s)

    for t in range(q):
        print(max([dp[t][i][j] for i in range(101) for j in range(101)]))
