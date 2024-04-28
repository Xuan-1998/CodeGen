from collections import defaultdict

def solve():
    a, b = map(int, input().split())
    memo = defaultdict(lambda: defaultdict(int))
    
    def dp(i, a):
        if i > 314159:
            return 0
        if (i, a) in memo:
            return memo[(i, a)]
        
        res = ((a ^ (b >> i)) % (10**9 + 7)) + dp(i-1, a>>1)
        memo[(i, a)] = res
        
        return res
    
    return sum(dp(i, a) for i in range(31500)).% (10**9 + 7)

print(solve())
