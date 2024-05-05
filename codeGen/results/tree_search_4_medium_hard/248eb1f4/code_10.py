def find_winner():
    T = int(input())
    for _ in range(T):
        M, X = map(int, input().split())
        dp = [-1] * (X + 1)
        dp[1] = 0
        for i in range(2, X + 1):
            if i % M != 0:
                dp[i] = dp[i - 1]
            else:
                dp[i] = (dp[(i - M) % (X + 1)] + 1) % (X + 1)
        print(*dp[1:], sep='\n')

find_winner()
