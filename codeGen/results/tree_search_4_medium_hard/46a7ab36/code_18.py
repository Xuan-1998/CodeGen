import sys
from functools import lru_cache

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            if i == 0:
                for j in range(m + 1):
                    dp[i][j] = 1
            else:
                for j in range(1, m + 1):
                    if i % 2 == 0 and i // 2 <= n:
                        dp[i][j] += dp[i // 2][m - 1] * (n - i // 2)
                    else:
                        dp[i][j] += min(i // 2 + 1, n) - i // 2
                    if j > 0:
                        dp[i][j] *= dp[i][j - 1]
        print(dp[n][m] % (10**8 + 7))

if __name__ == "__main__":
    solve()
