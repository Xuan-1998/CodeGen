import sys

def solve():
    T = int(input())
    MOD = 10**9 + 7
    dp = [[0] * (2001) for _ in range(2001)]

    for i in range(T):
        N, M = map(int, input().split())
        if N > 0 and M > 0:
            dp[N][M] = sum(dp[k][M-k] for k in range(N))
        print(dp[N][M] % MOD)

if __name__ == "__main__":
    solve()
