from collections import namedtuple

HareInfo = namedtuple('HareInfo', 'a b c')

def solve():
    n = int(input())
    hares = []
    for _ in range(3):
        row = [int(x) for x in input().split()]
        hares.append(HareInfo(*row))

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = hares[i - 1].c
        for j in range(1, i + 1):
            if j == 1:
                dp[i][j] = max(dp[i-1][j-1] + hares[i-1].a, dp[i-1][j])
            else:
                dp[i][j] = max(dp[i-1][j-1] + (hare_info.a if hare_info.b == 0 else hare_info.b) for hare_info in hares[:i])
        dp[i][i] = dp[i][i-1]

    print(max(dp[n]))

if __name__ == '__main__':
    solve()
