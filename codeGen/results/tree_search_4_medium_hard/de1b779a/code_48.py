import sys
from collections import defaultdict

def solve():
    n, m, c0, d0 = map(int, input().split())
    dp = [[-float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0] = [0] * (m + 1)

    stuffing_info = defaultdict(lambda: [0, 0, 0, 0])
    for i in range(m):
        ai, bi, ci, di = map(int, input().split())
        stuffing_info[i + 1] = [ai, bi, ci, di]

    for i in range(1, n + 1):
        for j in range(m + 1):
            if i <= c0:
                dp[i][j] = max(dp[i][j], dp[i][j - 1])
            else:
                for k in range(j):
                    ai, bi, ci, di = stuffing_info[k]
                    if i >= ai and i >= ci:
                        dp[i][j] = max(dp[i][j], dp[ai - ci][k - 1] + (i - ci) * di)
    
    print(max(dp[n]))

if __name__ == "__main__":
    solve()
