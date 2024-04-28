import sys

MOD = 10**9 + 7

def solve():
    a, b = map(int, input().split())
    dp = [[0] * (2 ** 20) for _ in range(32)]
    
    for i in range(1, 32):
        for j in range(1 << 19):
            if (j >> i) & 1:
                a <<= 1
            else:
                b <<= 1
            dp[i][j] = (dp[i - 1][j ^ (a & ((2 ** 19) - 1))] + b) % MOD
    
    return sum(dp[-1]) % MOD

print(solve())
