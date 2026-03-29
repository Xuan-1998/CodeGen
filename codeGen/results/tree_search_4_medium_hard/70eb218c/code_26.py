from functools import lru_cache

def solve():
    n, x = map(int, input().split())
    
    @lru_cache(None)
    def dp(i):
        if i == 0:
            return -1
        if i < len(str(x)):
            return 0
        
        last_digit = int(str(x)[-1])
        if last_digit < 10:
            return dp(i-1) + (1 if i > 1 else 0)
        return min(dp(i-1), dp(i-1)-1)
    
    return -1 if dp(n) == -1 else dp(n)

print(solve())
