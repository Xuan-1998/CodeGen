def calculate_sequencies():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))

        dp = [0] * (C + 1)
        dp[0] = 1

        for i in range(1, C + 1):
            for j in range(min(i, N), -1, -1):
                if U[j - 1] >= i:
                    dp[i] += dp[i - 1]
            for k in range(min(i, M), -1, -1):
                if L[k - 1] >= i:
                    dp[i] = (dp[i] + dp[i - 1]) % (10**9 + 7)

        print(*map(str, dp[C]), sep=' ')

calculate_sequencies()
