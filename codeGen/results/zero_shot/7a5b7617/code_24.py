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
                else:
                    sum_j = min(j, M)
                    for k in range(sum_j, -1, -1):
                        dp[i][j] += (k >= dp[i-1][sum_j-k+1] + 1) % 1000000000
        print(dp[N][M])

if __name__ == "__main__":
    solve()
