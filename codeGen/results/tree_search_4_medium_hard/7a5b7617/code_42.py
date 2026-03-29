import sys

mod = 1e9 + 7

def solve():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        dp[0][0] = 1
        for i in range(1, N + 1):
            for j in range(M + 1):
                if i == 1:
                    if j <= M:
                        dp[i][j] = 1
                else:
                    if sum(dp[i - 1]) <= M and sum(dp[i - 1]) + j <= M:
                        dp[i][j] = (dp[i][j - 1] + dp[i - 1][M]) % mod
        print((dp[N][M]) % mod)

if __name__ == "__main__":
    solve()
