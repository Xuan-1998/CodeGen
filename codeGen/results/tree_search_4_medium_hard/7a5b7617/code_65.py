from collections import defaultdict

def solve():
    T = int(input())
    dp_dict = defaultdict(int)

    for _ in range(T):
        N, M = map(int, input().split())
        if N == 0 or M == 0:
            print(1)
        elif N > M:
            print(0)
        else:
            dp = [[0] * (M + 1) for _ in range(N + 1)]
            for j in range(M + 1):
                dp[0][j] = 1
            for i in range(1, N + 1):
                for j in range(M + 1):
                    if j == 0:
                        continue
                    dp[i][j] = (M - dp[i-1][M]) + sum(dp[k][j-1] for k in range(i))
            print(dp[N][M] % (10**9 + 7))

if __name__ == "__main__":
    solve()
