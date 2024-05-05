import sys

def solve():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        prefix_sum = [0] * (N + 1)
        for i in range(1, N + 1):
            prefix_sum[i] = prefix_sum[i - 1] + M
        for i in range(1, N + 1):
            for j in range(M + 1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = sum(1 for k in range(j) if prefix_sum[i - 1] >= k and prefix_sum[i - 1] <= M)
        print(sum(dp[-1]) % (10 ** 9 + 7))

if __name__ == "__main__":
    solve()
