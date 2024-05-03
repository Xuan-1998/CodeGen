import sys

def solve():
    n, m = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        last_section = int(input()) - 1
        for j in range(m, -1, -1):
            if j == last_section:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j+1] + 1)
            else:
                dp[i][j] = dp[i-1][j+1] + 1

    print(min(dp[n]))

if __name__ == "__main__":
    solve()
