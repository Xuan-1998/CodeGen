import sys

def solve():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(M + 1):
                if i == 1:
                    dp[i][j] = 1
                elif j < M - sum(dp[i-1]):
                    dp[i][j] = (dp[i-1][M - sum(dp[i-1])] + 1) % (10**9 + 7)
                else:
                    dp[i][j] = dp[i-1][j]
        print(sum([sum(row) for row in dp]) % (10**9 + 7))

if __name__ == "__main__":
    solve()
