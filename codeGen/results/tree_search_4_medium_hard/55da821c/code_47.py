import sys

def solve():
    n, m = map(int, input().split())
    dp = [[0] * m for _ in range(n+1)]

    for i in range(1, n+1):
        s, x = map(int, input().split())
        for j in range(m):
            if j + 1 == s:
                dp[i][j] = min(dp[i-1][k] + 1 for k in range(m) if k != j)
            else:
                dp[i][j] = dp[i-1][j]

    print(min(dp[-1]))

if __name__ == "__main__":
    solve()
