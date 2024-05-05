def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))
        dp = [0] * (C + 1)
        dp[0] = 1
        for i in range(N):
            for j in range(C, U[i] - 1, -1):
                dp[j] = (dp[j] + dp[j-1]) % (10**9 + 7)
        for i in range(M):
            for j in range(C, L[i] - 1, -1):
                dp[j] = (dp[j] + dp[j-1]) % (10**9 + 7)
        print(*dp, sep=' ')
