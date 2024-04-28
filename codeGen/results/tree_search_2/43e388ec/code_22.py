import sys

def solve(a, b):
    MOD = 10**9 + 7
    
    memo = {}
    
    def dp(i, ab):
        if (i, ab) in memo:
            return memo[(i, ab)]
        
        result = 0
        for bit in range(31, -1, -1):
            if ((ab >> bit) & 1):
                if i % 2 == 0:
                    result ^= a & ((1 << bit) - 1)
                else:
                    result ^= (a >> 1)
        
        memo[(i, ab)] = result
        return result
    
    result = 0
    for i in range(315):
        result += dp(i, a & b)
    
    return str(result % MOD)

a, b = map(int, input().split())
print(solve(a, b))
