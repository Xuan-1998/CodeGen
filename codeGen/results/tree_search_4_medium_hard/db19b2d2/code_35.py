import sys
from math import comb

def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))

    dp = [[0.0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for k in range(min(i, n)+1):
            if k == 0:
                dp[i][k] = 1.0
            else:
                dp[i][k] = (dp[i-1][k-1] * comb(s[i-1], k) / comb(n+k-1, k)) + (1 - dp[i-1][k]) if k <= s[i-1] else 0.0

    res = 0.0
    for k in range(1, n+1):
        res += dp[h][k]

    print(res)

if __name__ == "__main__":
    solve()
