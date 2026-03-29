import sys

def solve():
    n, m, c0, d0 = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    c = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(m):
        ai, bi, ci, di = map(int, input().split())
        for j in range(min(n, ci), -1, -1):
            if j >= bi:
                dp[j][i+1] = max(dp[j][i], dp[j-bi][i] + di)
            c[j][i+1] = min(c[j][i], ci)

    print(max(dp[n][m]))

if __name__ == "__main__":
    solve()
