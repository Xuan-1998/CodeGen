import sys

def solution():
    a, b = map(int, input().split())
    
    MOD = 10**9 + 7
    
    dp = [[0] * (b.bit_length() + 1) for _ in range(a.bit_length() + 1)]
    for i in range(a.bit_length() + 1):
        if a & (1 << i):
            dp[i][0] = (a >> i) % MOD
        else:
            dp[i][0] = (b >> i) % MOD
    
    for j in range(b.bit_length() + 1):
        if b & (1 << j):
            dp[0][j] = (b >> j) % MOD
        else:
            dp[0][j] = (a >> j) % MOD
    
    for i in range(1, a.bit_length() + 1):
        for j in range(1, b.bit_length() + 1):
            if ((a >> i) & 1) == ((b >> j) & 1):
                dp[i][j] = (dp[i-1][j-1] + (a >> i)) % MOD
            else:
                dp[i][j] = (dp[i-1][j-1] + (b >> j)) % MOD
    
    print((dp[a.bit_length()][b.bit_length()] + a) % MOD)

if __name__ == "__main__":
    solution()
