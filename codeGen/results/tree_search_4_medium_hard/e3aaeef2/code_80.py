import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        dp = [[0] * (m + 1) for _ in range(10)]
        for i in range(1, 10):
            dp[i][0] = 1
        for j in range(1, m + 1):
            for i in range(10):
                if i > 0:
                    dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1]) + (i != 9)
                else:
                    dp[i][j] = dp[9][j - 1]
        print((dp[n % 10][m]).__mod__(10**9 + 7))

if __name__ == "__main__":
    solve()
