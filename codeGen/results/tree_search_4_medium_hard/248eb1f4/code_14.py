def solve():
    T = int(input())
    for _ in range(T):
        M, X = map(int, input().split())
        dp = [0] * (X + 1)
        for i in range(X, M - 1, -1):
            if i % M == 0:
                dp[i] = (i - 1) % (X + 1)
            else:
                dp[i] = (dp[i - M] + M - 1) % (X + 1)
        print(dp[X])
