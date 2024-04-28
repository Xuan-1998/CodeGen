import sys

def solve():
    a, b = map(int, input().split())
    
    dp = [[0] * (31) for _ in range(21)]
    
    for i in range(log2(a) + 1):
        bit = ((a >> i) & 1)
        
        for j in range(log2(10**9+7) + 1):
            dp[i][j] = dp[i-1][j]
            
            if (i > 0 and j >= log2(b) - i):
                dp[i][j] += bit * ((b >> (log2(b) - i)) & 1)
            
            dp[i][j] %= (10**9+7)

    ans = 0
    for j in range(log2(10**9+7) + 1):
        ans += dp[20][j]
    
    print(ans % (10**9+7))

def log2(x):
    return int(x.bit_length() - 1)
