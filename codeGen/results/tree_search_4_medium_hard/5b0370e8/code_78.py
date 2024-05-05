import sys

dp = [[0] * (2**18 + 1) for _ in range(2**18 + 1)]

def solve():
    n, k = map(int, input().split())
    res = 0
    for i in range(n):
        a = int(input(), 2)
        for j in range(k - 1, -1, -1):
            and_val = (a >> j) & 1
            xor_val = (a >> j) ^ 1
            dp[a][j] += dp[a & ~((1 << j) - 1)][j]
            if and_val == 0:
                res = max(res, dp[a][j])
            else:
                res += dp[a][j]
    print(res % (10**9 + 7))

solve()
