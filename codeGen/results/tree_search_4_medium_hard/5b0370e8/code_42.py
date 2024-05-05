def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (1 << k) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for mask in range(1 << k):
                if mask & (mask - 1):  # check if there's a set bit
                    dp[i][mask] = sum(dp[j][mask & k] for j in range(i)) % (10**9 + 7)
                else:
                    dp[i][mask] = 0
        print(sum(dp[n]) % (10**9 + 7))
