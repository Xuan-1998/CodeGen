import sys
from collections import defaultdict

# Define constants
MOD = 10**9 + 7

def solve():
    t = int(input())
    
    for _ in range(t):
        n, k = map(int, input().split())
        
        dp = [[0] * (1 << k) for _ in range((1 << k) + 1)]
        dp[0][0] = 1
        
        for j in range(1 << k):
            for i in range((1 << k), -1, -1):
                if i & j:
                    dp[i ^ j][j] += dp[i][j]
                    dp[i ^ j][j] %= MOD
                    
        and_count = 0
        xor_sum = 0
        
        for _ in range(n):
            num = int(input())
            
            while k > 0:
                bit = (1 << (k - 1))
                if num & bit:
                    and_count |= bit
                    xor_sum ^= bit
                    k -= 1
                else:
                    break
            
            dp[and_count][xor_sum] += 1
            dp[and_count][xor_sum] %= MOD
        
        print((dp[(1 << k) - 1][0] - 1 + MOD) % MOD)

if __name__ == "__main__":
    solve()
