import sys

def solve():
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())

    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        dp[i][0] = 1

    for i in range(1, N + 1):
        for j in range(min(i + 1, M) + 1):
            dp[i][j] = sum(dp[k][min(j + 1, k)] for k in range(i))

    print(sum(dp[N][k] for k in range(M + 1)) % 1000000000)

if __name__ == "__main__":
    solve()
