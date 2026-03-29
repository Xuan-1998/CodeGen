def solution():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))

        # Initialize the dp array
        dp = [0] * (C + 1)
        dp[0] = 1

        for u in U:
            for i in range(C, u - 1, -1):
                dp[i] = (dp[i] + dp[i - 1]) % (10**9 + 7)

        for l in L:
            for i in range(C, l - 1, -1):
                dp[i] = (dp[i] + dp[i - 1]) % (10**9 + 7)

        # Print the result
        print(*[dp[i] for i in range(C + 1)], sep=' ')

solution()
