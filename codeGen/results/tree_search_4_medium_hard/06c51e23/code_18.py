import sys

def solve():
    n, t = map(int, input().split())
    dp = [[0] * (n + 1) for _ in range(t + 1)]

    for i in range(n + 1):
        for k in range(min(i, t) + 1):
            if i == 0:
                dp[k][i] = 0
            elif k <= i:
                dp[k][i] = max(dp[max(0, k - 1)][i - 1], round(float(''.join(map(str, [int(x) for x in input().split('.')[1].split(',')]))), k))
            else:
                dp[k][i] = dp[k][i - 1]

    print(int(round(dp[t][n], 0)))

solve()
