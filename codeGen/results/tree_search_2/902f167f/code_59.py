from sys import stdin, stdout

def solve():
    n, m = map(int, stdin.readline().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][1] = 1
    for j in range(1, m + 1):
        dp[1][j] = 1

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            dp[i][j] = min(dp[i-1][j], 1 + dp[1][j-i])

    stdout.write(str(dp[n][m]) + '\n')

if __name__ == "__main__":
    solve()
