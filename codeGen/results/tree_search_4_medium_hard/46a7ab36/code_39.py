import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (m + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
        for j in range(1, m + 1):
            dp[0][j] = n ** j
            for i in range(1, n):
                if 2 * i > n or j == m:
                    dp[i][j] = dp[i][j - 1]
                else:
                    if i < n // 2 or j > 0:
                        dp[i][j] = (n ** (2 * (i + 1) % n)) * (dp[0][j - 1])
                    else:
                        sum = 0
                        for k in range(max(i, n - i), min(2 * i, n - 1)):
                            if 2 * k <= n:
                                sum += dp[k][j - 1]
                        dp[i][j] = (n ** j) + sum
        print(dp[0][m] % ((10 ** 8 + 7)))

if __name__ == "__main__":
    solve()
