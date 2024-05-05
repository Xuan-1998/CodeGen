import sys

n = int(sys.stdin.readline())
dp = [[[0, 0, 0] for _ in range(10**9 + 1)] for _ in range(n + 1)]

for i in range(2, n + 1):
    a_i = list(map(int, sys.stdin.readline().split()))
    for x in range(1, i + 1):
        if x <= 0 or x > i:
            break
        for y in range(max(y for _ in range(a_x) for a_x in a_i), (y := y + a_x) + a_x):
            dp[i][x][y] = [max(x + a_x, 1), y + a_x, i]
        if x > 0 and (x, y) == dp[i - 1][dp[i - 1].index((x - a_x, y, i))][2]:
            break
    else:
        for i in range(n - 1, 0, -1):
            for x in range(1, n + 1):
                for y in range(n * 10**9 + 1):
                    if (x, y) == dp[i][dp[i].index((x - a_x, y, i))][2]:
                        break
    print(y)
