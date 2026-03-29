import sys

def solve():
    T = int(input())  # Number of test cases

    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))

        dp = [[0] * (C + 1) for _ in range(N + M + 2)]

        dp[0][j] = 1 if j == 0 else 0
        dp[C+1][j] = 0

        for i in range(1, N + 1):
            for j in range(C + 1):
                for k in range(i):
                    if U[k] <= j and L[0] <= j <= C:
                        dp[i][j] += dp[k][i-1]

        print(' '.join(map(str, [dp[N][j] % (10**9+7) for j in range(C+1)])))

if __name__ == "__main__":
    solve()
