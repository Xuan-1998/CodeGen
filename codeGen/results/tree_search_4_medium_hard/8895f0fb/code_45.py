import sys
from collections import namedtuple
from functools import lru_cache

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    
    # Initialize DP table
    dp = [[0, 0] for _ in range(N + 1)]
    
    @lru_cache(None)
    def carry_expected(n):
        if n == 0:
            return 0.5
        
        res = [0, 0]
        
        # No carry from the previous addition
        no_carry_res = (carry_expected(n - 1) * ((A < 10 ** (n - 1)) and (B < 10 ** (n - 1)))) + (carry_expected(n - 1) if A >= 5 or B >= 5 else 0)
        
        # Carry from the previous addition
        carry_res = no_carry_res + ((carry_expected(n - 1) - no_cary_res) * ((A >= 10 ** (n - 1)) and (B >= 10 ** (n - 1))))
        
        res[0] = min(no_carry_res, carry_res)
        res[1] = max(no_carry_res, carry_res)
        
        return sum(res) / 2
    
    print(carry_expected(N))
