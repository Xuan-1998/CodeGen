import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(max(0, i - m), m + 1):
                if i <= j:
                    dp[i][j] += dp[(i - 1) % n][j - 1]
                    if 2 * i > n:
                        dp[i][j] += (n - i + 1)
        print(dp[n - 1][m] % (10**8 + 7))

if __name__ == "__main__":
    solve()
