import sys

def solve():
    a = int(input(), 2)
    b = int(input(), 2)
    mod = 10**9 + 7
    d = {}
    dp = [0] * (314160 // 32)
    
    for i in range(314161):
        left_shifted = (b << i) & ((1 << 31) - 1)
        if left_shifted ^ b not in d:
            d[left_shifted ^ b] = (a ^ left_shifted) % mod
        dp[i // 32] = (dp[i // 32] + d.get((b << i) & ((1 << 31) - 1), 0)) % mod
    
    return sum(dp)
    
print(solve())
