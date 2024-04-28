import sys

MOD = int(1e9 + 7)

def solve():
    a, b = [int(x) for x in input().split()]
    
    dp = [[0] * (len(bin(b)) - 2) for _ in range(len(bin(a)) - 2)]
    
    for i in range(len(bin(a)) - 2):
        for j in range(len(bin(b)) - 2):
            if j >= i:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = (dp[i-1][j] + (1 << (i-1))) % MOD
    
    return sum(dp[i][j] for i in range(len(bin(a)) - 2) for j in range(len(bin(b)) - 2))

print(solve())
