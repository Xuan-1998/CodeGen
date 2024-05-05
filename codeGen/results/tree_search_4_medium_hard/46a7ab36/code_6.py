import math

def calculate_words():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        k = m // 2 + (m % 2)
        mod = 10**9 + 7
        dp = [[0] * (n+1) for _ in range(k+1)]
        dp[0][0] = 1

        for i in range(1, n+1):
            for j in range(min(i, k), -1, -1):
                if i < n and i % 2 == 1:
                    dp[j][i] = (dp[j-1][i-1] * (n-i)) % mod
                else:
                    dp[j][i] = (dp[j][i-1] + dp[j-1][i-1]) % mod

        print((dp[0][m-1]) % mod)

calculate_words()
