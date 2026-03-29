def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))

        dp = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(N + 1):
            dp[i][0] = 1
        for j in range(M + 1):
            dp[0][j] = 1

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                for k in range(max(0, j - i), min(i, j) + 1):
                    dp[i][j] += dp[min(i-1,k)][abs(j-k)]
                    dp[i][j] %= (10**9 + 7)

        print(*dp[N][M:], sep=' ')
